import argparse
import os
from funcs.sn_scan import sn
from funcs.scan import scan

parser = argparse.ArgumentParser()

parser.add_argument('host', type=str, help='target host')
parser.add_argument('-sn', help='scan if host is up', action='store_true')
parser.add_argument('-T0', help='very small timeout (0.10ms)', action='store_true')
parser.add_argument('-T1', help='default timeout (1s)', action='store_true')
parser.add_argument('-T2', help='long timeout (3s)', action='store_true')
parser.add_argument('-p-', help='scan all 65536 ports', action='store_true')

args = parser.parse_args()

ascii_art = r'''
 ____                               ____           _     _               
| __ )  __ _ _ __  _ __   ___ _ __ / ___|_ __ __ _| |__ | |__   ___ _ __ 
|  _ \ / _` | '_ \| '_ \ / _ \ '__| |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
| |_) | (_| | | | | | | |  __/ |  | |_| | | | (_| | |_) | |_) |  __/ |   
|____/ \__,_|_| |_|_| |_|\___|_|   \____|_|  \__,_|_.__/|_.__/ \___|_|   


'''

if __name__ == '__main__':
    timeout = 1
    ports = range(1023) if not args.p_ else range(65536)

    if args.T0:
        timeout = 0.10
    if args.T2:
        timeout = 3

    os.system('cls') if os.name == 'nt' else os.system('clear')
    print(ascii_art)
    print("Starting BannerGrabber 1.0 ...")

    if args.sn:
        try:
            sn(args.host, timeout, ports)
        except Exception as e:
            pass
    else:
        try:
            scan(args.host, timeout, ports)
        except Exception as e:
            pass
