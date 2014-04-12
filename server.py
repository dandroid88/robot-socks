#!/usr/bin/env python
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
from robot import ctrl

class Position:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return str(self.x) + ' ' + str(self.y)

    def __str__(self):
         return str(self.x) + ' ' + str(self.y)

class Robot(WebSocketApplication):
    def on_open(self):
        print "Connection opened"

    def on_message(self, message):
        handle_message(message)

    def on_close(self, reason):
        print reason

def handle_message(message):
    try:
        message_type, value = message.split('.', 1)
        if 'm' in message_type:
            move(value)
    except Exception as e:
        print 'Failure' + str(e)

def move(message_value):
    if 'forward' in message_value:
        ctrl.forward()
    if 'backword' in message_value:
        ctrl.backword()
    if 'spin_left' in message_value:
        ctrl.spin_left()
    if 'spin_right' in message_value:
        ctrl.spin_right()
    if 'stop' in message_value:
        ctrl.stop()
    print message_value


def _calculate_speed(current_position):
    """ Distnace from center of touchpage """
    return None

def _calculate_angle(current_position):
    """Trig function operating on the y/x offset from center"""
    return None

WebSocketServer(('', 8000), Resource({'/': Robot})).serve_forever()
