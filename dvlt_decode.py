import sys, os, re
import struct
from datetime import datetime
from io import BytesIO
import subprocess
from pprint import pprint
import pickle

class DevialetDecoder:
    def __init__(self):
        self.magics = [0xc2, 0xc3]
        self.magic_headers = [b'\xc2\x01\x00\x00\x00\x00', b'\xc3\x01\x00\x00\x00\x00']

    def decode_protobuf(self, data):
        process = subprocess.Popen(['protoc', '--decode_raw'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process.stdin.write(data)
        process.stdin.close()
        ret = process.wait()
        if ret == 0:
            return {
                "raw": data,
                "protoc": process.stdout.read().decode()
            }
        else:
            return {
                "raw": data,
                "protoc": "",
                "error": 'Failed to parse: ' + ' '.join('{:02x}'.format(x) for x in data)
            }

    def decode_section(self, section):
        obj = {
            'magic': section[0]['firstbyte'],
            # 'raw_fields': section
        }

        # Delimiter, always empty
        i = 0
        if len(section[i]['data']) != 0:
            obj.setdefault('error', []).append('Weird, field {}/{} of length {} instead of {}'.format(
                i, len(section), len(section[i]['data']), 0))
        i += 1

        # Extra field (+ delimiter) that doesnt decode into protobuf, some kind of uid?
        if len(section) == 5 and len(section[i]['data']) == 16 and len(section[i+1]['data']) == 0:
            obj['uid'] = section[i]['data'].hex()
            i += 2
        
        # Remaining fields should all be protobufs
        while i < len(section):
            obj.setdefault('protobufs', []).append(self.decode_protobuf(section[i]['data']))
            if section[i]['firstbyte'] != obj['magic']:
                obj.setdefault('error', []).append('Weird, magic mismatch {} != {}'.format(
                    section[i]['firstbyte'], obj['magic']))
            i += 1

        return obj

    def decode_packet(self, packet):
        new_section = True
        sections = []
        ret = {'sections': []}

        try:
            field_header = packet.read(6)
            firstbyte = field_header[0]
            while len(field_header) == 6 and firstbyte in self.magics:
                firstbyte, same_section, field_length = struct.unpack('>BBL', field_header)
                field_data = packet.read(field_length)
                field = { 'firstbyte': firstbyte, 'data': field_data }

                if new_section:
                    sections.append([field])
                else:
                    sections[-1].append(field)           

                field_header = packet.read(6)
                # when second byte of section header is 0, next field is part of new section
                new_section = not same_section

            rest = packet.read()
            if len(field_header) != 0 or firstbyte not in self.magics or rest:
                 ret.setdefault('error', []).append('Found garbage at end of packet: header={} rest={}'.format(
                    field_header.hex(), ' '.join('{:02x}'.format(x) for x in rest)))

            for section in sections:
                ret['sections'].append(self.decode_section(section))
        except IndexError as e:
            print("Error: Empty or too short packet: {} {}".format(type(e), e))

        return ret

    def is_whole_packet(self, packet):
        field_header = packet.read(6)
        firstbyte = field_header[0]

        while len(field_header) == 6 and firstbyte in self.magics:
            firstbyte, same_section, field_length = struct.unpack('>BBL', field_header)
            field = packet.read(field_length)

            field_header = packet.read(6)

        return (field_length == len(field) and len(field_header) == 0)

    def decode_capture(self, iter):
        packets = []
        last_packet_whole = True
        print('.')

        for packet in iter:
            # print(packet['direction'], packet['data'].hex())
            if not last_packet_whole:
                packets[-1]['data'] += packet['data']
                packets[-1]['merged'] += 1
                last_packet_whole = self.is_whole_packet(BytesIO(packets[-1]['data']))

            elif packet['data'][:6] in self.magic_headers:
                packets.append(packet)
                last_packet_whole = self.is_whole_packet(BytesIO(packet['data']))

            else:
                packet['error_unknown'] = 'Unknown packet {}'.format(
                        ' '.join('{:02x}'.format(x) for x in packet['data']))
                packets.append(packet)
                last_packet_whole = True

        for packet in packets:
            packet.update(self.decode_packet(BytesIO(packet.pop('data'))))

        return packets

    def decode_sessions(self):
        raise NotImplementedError()

class AndroidCaptureDecoder(DevialetDecoder):
    def __init__(self, dirs):
        DevialetDecoder.__init__(self)
        self.dirs = dirs

    def packet_iter(self, filename):
        i = 0
        with open(filename, 'rb') as file:
            header = file.read(16)
            while len(header) == 16:
                tstamp, direction, pad1, pad2, length, pad3 = struct.unpack('<qBBHhH', header)
                packet = {
                    'time': datetime.fromtimestamp(tstamp / 1000),
                    'direction': direction, #'->' if direction else '<-'
                    'number': i,
                    'length': length,
                    'merged': 1,
                    'data': file.read(length)
                }
                header = file.read(16)
                i += 1
                yield packet

    def decode_session(self, dirname):
        session = {
            'name': dirname,
            'captures': [{
                'name': capture,
                'port': re.match('^[0-9]+_([0-9]+).dat$', capture).group(1),
                'start_time': datetime.fromtimestamp(int(re.match('^([0-9]+)_[0-9]+.dat$', capture).group(1))/1000),
                'packets': self.decode_capture(self.packet_iter(os.path.join(dirname, capture)))
            } for capture in sorted(os.listdir(dirname))]
        }

        session['start_time'] = min(capture['start_time'] for capture in session['captures'])
        session['number_of_captures'] = len(session['captures'])

        return session

    def decode_sessions(self):
        return [self.decode_session(dir) for dir in self.dirs]

if __name__ == '__main__':

    decoder = AndroidCaptureDecoder(['sess' + str(i+1) for i in range(5)])
    sessions = decoder.decode_sessions()

    dump_file = open('all_decoded2.pickle', 'wb')
    pickle.dump(sessions, dump_file)