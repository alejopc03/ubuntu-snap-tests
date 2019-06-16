#!/usr/bin/env python
# coding=utf-8
import os

def main():
    command = 'hostnamectl'
    deviceInfo = os.popen(command).read()

    message = "Device Information: \n{0}".format(deviceInfo)
    print(message)

if __name__ == '__main__':
    main()
