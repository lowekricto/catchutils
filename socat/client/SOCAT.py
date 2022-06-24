# !/usr/bin/python3
# filename：SOCAT.py


# C命令标识: \xff\xff\x6b\x6d\x78\xff
# 命令标识
# C命令标识
import sys
import socket
from ctypes import sizeof
C_COMMAND_IDE = b"\xff\xff\x6b\x6d\x78\xff"

C_COMMAND_IDE_1 = b"\xff\x43\x4b\x4f\x4e\x45\xff"
C_COMMAND_IDE_2 = b"\xff\x43\x4b\x54\x57\x4f\xff"
C_COMMAND_IDE_3 = b"\xff\x43\x4b\x54\x48\x52\xff"
C_COMMAND_IDE_4 = b"\xff\x43\x4b\x46\x4f\x52\xff"
C_COMMAND_IDE_5 = b"\xff\x43\x4b\x46\x49\x56\xff"

C_COMMAND_IDE_ITEM = b"\xff\x4b\x49\x54\x45\x4d\xff"


SOCAT_PORT = 64335
BUFFERSIZE = 256

# KALOS_HOST = '101.42.95.33'
KALOS_HOST = 'www.kricto.cn'
# KALOS_HOST = "144.255.17.38"
# KALOS_HOST = '192.168.123.227'

# KALOS_HOST = '127.0.0.1'
KALOS_PORT = 64335


def getcount(list):
    index = 0
    for x in list:
        index += 1
    return index


# get a socket
def get_asocket():

    # create socat object
    socat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socat.connect((KALOS_HOST, KALOS_PORT))

    return socat


def makeSendBodylist(commandBody):
    bcommandBody = commandBody

    ret = []
    tem = bytearray()
    index = 0

    for x in bcommandBody:
        if index <= BUFFERSIZE:
            tem += bytearray([x])
            index += 1
        if index == BUFFERSIZE:
            index = 0
            ret.append(tem)
            tem = bytearray()

    retcount = getcount(ret)
    temcount = len(tem)

    if retcount == 0:
        ret.append(tem)
        tem = bytearray()
        index = 0
    if (retcount != 0) & (temcount != 0):
        ret.append(tem)
        tem = bytearray()
        index = 0

    return ret


def addheader_item(x):
    ret = C_COMMAND_IDE_ITEM
    ret += x
    ret += C_COMMAND_IDE_ITEM
    return ret


def makecommandBody(commandBodySet, deep=0):
    ret = bytearray()
    C_COMMAND_IDE_X = bytearray()

    if deep != 0:
        switch = {
            "1": C_COMMAND_IDE_1,
            "2": C_COMMAND_IDE_2,
            "3": C_COMMAND_IDE_3,
            "4": C_COMMAND_IDE_4,
            "5": C_COMMAND_IDE_5,
        }
        C_COMMAND_IDE_X = switch[str(deep)]

    ret += C_COMMAND_IDE_X

    for x in commandBodySet:
        deeps = deep
        # 如果是item
        if type(x) == type(""):
            xx = str(x).encode("utf-8")
            ret += addheader_item(xx)
        if type(x) == type([]):
            deeps += 1
            ret += makecommandBody(x, deeps)

    ret += C_COMMAND_IDE_X
    return ret


def send(commandID, commandBodySet):

    commandBody = makecommandBody(commandBodySet)

    # print(commandBody)

    socatclient = get_asocket()

    command = (commandID).encode("utf-8")
    command += C_COMMAND_IDE
    stopCommand = "kk".encode("utf-8")

    commandBodyList = makeSendBodylist(commandBody)

    ret = socatclient.send(command)

    for x in commandBodyList:
        # commandCut = str(x).encode("utf-8")
        commandCut = x
        ret = socatclient.send(commandCut)

    ret = socatclient.send(stopCommand)

    rep = socatclient.recv(BUFFERSIZE)

    return str(rep, "utf-8")
