import termcolor
from pprint import pformat

DEFAULT_LOGLEVEL = 5


def print_error(txt, *args, loglevel=DEFAULT_LOGLEVEL):
    if loglevel > 0:
        print(termcolor.colored("Error: " + str(txt).format(*args), "red"))


def print_warning(txt, *args, loglevel=DEFAULT_LOGLEVEL):
    if loglevel > 2:
        print(termcolor.colored("Warning: " + str(txt).format(*args), "yellow"))


def print_info(txt, *args, loglevel=DEFAULT_LOGLEVEL):
    if loglevel > 3:
        print(termcolor.colored("Info: " + str(txt).format(*args), "blue"))


def print_data(txt, *args, loglevel=DEFAULT_LOGLEVEL):
    if loglevel > 1:
        print(termcolor.colored(txt, "green"))
        for arg in args:
            for line in pformat(arg).split('\n'):
                print(termcolor.colored("\t"+line, "white"))
        # print(termcolor.colored(str(txt).format(*[pformat(arg) for arg in args])   , "green"))
