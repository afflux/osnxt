"""
    Intended to log output from the NXT. Install the library with `pip install jaraco.nxt`.

    Is currently capable of connecting to, sending and receiving messages from the device,
    but the behavior is inconsistent and unreliable right now. Needs more work.

    Documentation for the library is mostly nonexistent, but the code is largely readable
    and can be found online here: https://bitbucket.org/jaraco/jaraco.nxt/src/f57211f87edf/jaraco/nxt/?at=default

"""

from jaraco.nxt import Connection
from jaraco.nxt.messages import *
import time

print "Establishing connection..."
conn = Connection(3)


def get_port(port, cls):
    if isinstance(port, basestring):
        port = getattr(cls, port)
    assert port in cls.values()
    return port


def cycle_motor(conn, port):
    "Turn the motor one direction, then the other, then stop it"
    port = get_port(port, OutputPort)
    cmd = SetOutputState(port, motor_on=True, set_power=100, run_state=RunState.running)
    conn.send(cmd)
    time.sleep(2)
    cmd = SetOutputState(port, motor_on=True, set_power=-100, run_state=RunState.running)
    conn.send(cmd)
    time.sleep(2)
    cmd = SetOutputState(port)
    conn.send(cmd)

cycle_motor(conn, 'b')
