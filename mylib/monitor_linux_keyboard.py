#!/usr/bin/env python
#coding: utf-8

'''
小程序，检测linux键盘按键

'''

from evdev import InputDevice
from select import select

def detectInputKey(key):
    dev = InputDevice('/dev/input/event2')
    while True:
        select([dev], [], [])
        for event in dev.read():
           if (event.value == 1 or event.value == 0) and event.code != 0:
                i=event.code
                print "Key: %s Status: %s" % (event.code, "pressed" if event.value else "release")
                print "Key: %s Status: %s" % (key[i], "pressed" if event.value else "release")


key_num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 87, 88, 96, 97,98 , 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 119, 125, 126, 127]
key_means=['ESC', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace', 'tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'Enter', 'Ctrl_left', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '`', 'Shift_left', '\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ' ', '.', '/', 'Shift_right', '*', 'Alt_left', 'Blank', 'CapsLock', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'NumLock', 'ScrollLock', '7', '8', '9', '-', '4', '5', '6', '+', '1', '2', '3', '0', '.', 'F11', 'F12', 'Enter', 'Ctrl','/' , 'PRINTSCREEN', 'Alt', 'home', 'Up', 'PageUp', 'End', 'left', 'right', 'down', 'PageDown', 'insert', 'delete', 'PauseBreak', 'Windows_left', 'Windows_right', 'paste']
key_val=dict(zip(key_num,key_means))

detectInputKey(key_val)