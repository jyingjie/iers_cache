#!/usr/bin/env python

import sys, os
import shutil
import random
import subprocess
import socket

from datetime import datetime
from astropy.utils.iers import conf
from astropy.utils import iers
from astropy.time import Time

def check_port(port, host='localhost'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        is_use = True if s.connect_ex((host, port)) == 0 else False
    return is_use

class Server:
    def __init__(self, port_range=(7000, 8887), max_try=10):
        port = random.randint(*port_range)
        for i in range(max_try):
            if check_port(port):
                port += 1
            else:
                break
        command = [sys.executable, '-m', 'http.server', '--directory', os.path.dirname(os.path.realpath(__file__)), '--bind', '127.0.0.1', str(port)]
        process = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        self.port = port
        self.process = process
        
    def close(self,):
        self.process.terminate()

def gen_finals2000A_cache():
    # conf.iers_auto_url = 'http://localhost' # for test
    ser = Server()
    conf.iers_auto_url_mirror = f'http://localhost:{ser.port}/files/finals2000A.all'
    try:
        Time(datetime.now(), format='datetime').ut1
        print("finals2000A cache generated.")
        ser.close()
        return 0
    except Exception as e:
        print(e)
        ser.close()
        return 1
    
def mv_file():
    dir_tar = os.path.join(os.path.dirname(iers.__file__),'data')
    print(f'copying files/eopc04_IAU2000.62-now to {dir_tar}')
    shutil.copy('files/eopc04_IAU2000.62-now', dir_tar)
    print(f'copying files/Leap_Second.dat to {dir_tar}')
    shutil.copy('files/Leap_Second.dat', dir_tar)
    
if __name__ == '__main__':
    
    mv_file()
    gen_finals2000A_cache()
    
    