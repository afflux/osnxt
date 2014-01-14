"""
    Intended to log output from the NXT. Install the library with `pip install jaraco.nxt`.

    Is currently capable of connecting to, sending and receiving messages from the device,
    but the behavior is inconsistent and unreliable right now. Needs more work.

    Documentation for the library is mostly nonexistent, but the code is largely readable
    and can be found online here: https://bitbucket.org/jaraco/jaraco.nxt/src/f57211f87edf/jaraco/nxt/?at=default

"""

from jaraco.nxt import Connection
from datetime import datetime
import struct
import time
import sys

PORT = 3
if sys.platform == 'linux2':
    PORT = '/dev/rfcomm0'

def log():
    with open('bluetooth.log', 'w') as log_file:
        print("Establishing connection...")
        conn = Connection(PORT, timeout=5)
        print('Logging output...')
        while True:
            print('Listening for output...')
            try:
                resp = conn.receive()
            except struct.error:
                print("Timed out")
                conn.close()
                time.sleep(1)
                conn.open()
            else:
                msg = parse_message(resp)
                print msg
                if msg.startswith('DISTANCE'):
                    log_file.write('%s %s\n' % (datetime.now().time(), msg))


def parse_message(msg):
    raw_content = msg.payload
    (msg_length,) = struct.unpack('B', raw_content[0])
    return raw_content[1:msg_length + 1]

if __name__ == '__main__':
    log()
