# !/usr/bin/python3
# filename：SOCAT.py

import socket
import sys
from exec import EXEC
from common import LOGGER
from socat import PARSERS as p

SOCAT_PORT = 64335
MAXLINKS = 25
HOSTIP = '0.0.0.0'
BUFFERSIZE = 100


logger = LOGGER.getlogger()


def socat():
    # create socat object
    socat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind port
    socat.bind((HOSTIP, SOCAT_PORT))

    # MAX link
    socat.listen(MAXLINKS)

    print("socat listen flow !!!")

    messionNo = 0

    while True:
        socatclient, addr = socat.accept()
        logger.info("1.1.1 收到新的连接 MessionNo = "+str(messionNo) +
                    " IPADDR = "+str(addr[0])+' SRC PORT = '+str(addr[1]))
        req = bytearray()
        while True:
            req += socatclient.recv(BUFFERSIZE)

            if(req[-2:].decode('utf-8', 'ignore') == 'kk'):
                break

        CMDID, CMDBODY = p.parsers(req)

        checked, res = EXEC.exec(socatclient, CMDID, CMDBODY)

        if(not checked):
            logger.warn("1.1.99 新的连接 MessionNo = " +
                        str(messionNo) + "出现异常处理失败!!!")

        socatclient.clos