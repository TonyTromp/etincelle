from datetime import datetime
import time
from dvlt_pool import Devialet, DevialetController
from dvlt_output import print_info, print_data
from dvlt_client import WhatsUpClient
from dvlt_server import DevialetServer
from dvlt_discovery import DevialetDiscovery
from queue import Queue

# import stacktracer
# stacktracer.trace_start("trace.html", interval=5, auto=True)


discovered = Queue()
dscvr = DevialetDiscovery(discovered)
dscvr.start()

serial, dvlt_addr = discovered.get(block=True)


def callback_test(arg):
    print_data("Callback with", arg)

# Open a WhatsUp connection
wu_client = WhatsUpClient(name="WhatsUp", addr=dvlt_addr, port=24242, start_time=datetime.now())
wu_client.open()
wu_client.start()
# wu_client.keep_receiving(timeout=2)
# reg.propertyGet(cmm_ctrl, Devialet.CallMeMaybe.Empty(), callback_test)

# tmf_client = DevialetClient(name='TooManyFlows Configuration', addr=dvlt_addr, port=37610, start_time=datetime.now())
# tmf_client.open()
# tmf_conf = Devialet.TooManyFlows.Configuration(tmf_client)
# tmf_ctrl = DevialetController(tmf_conf)
# tmf_conf.propertyGet(tmf_ctrl, Devialet.CallMeMaybe.Empty(), callback_test)
# tmf_client.keep_receiving()


wu_srv = DevialetServer(port=24242)
wu_srv.open()
dscvr.start_advertising()
wu_srv.start()


def pingback(arg):
    print_info("Pong <--")

try:
    while True:  # ~ 20 ms round-trip for pings
        time.sleep(1)
        print_info("Ping -->")
        wu_client.conn.ping(DevialetController(wu_client.conn), Devialet.CallMeMaybe.Empty(), pingback)
except KeyboardInterrupt:
    wu_client.shutdown()
    wu_srv.shutdown()
    dscvr.shutdown()

    print_info('join()ing client...')
    wu_client.join()
    print_info('join()ing server...')
    wu_srv.join()
    print_info('join()ing discovery..')
    dscvr.join()
