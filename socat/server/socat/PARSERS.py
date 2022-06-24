

C_COMMAND_IDE = b"\xff\xff\x6b\x6d\x78\xff"

C_COMMAND_IDE_1 = b"\xff\x43\x4b\x4f\x4e\x45\xff"
C_COMMAND_IDE_2 = b"\xff\x43\x4b\x54\x57\x4f\xff"
C_COMMAND_IDE_3 = b"\xff\x43\x4b\x54\x48\x52\xff"
C_COMMAND_IDE_4 = b"\xff\x43\x4b\x46\x4f\x52\xff"
C_COMMAND_IDE_5 = b"\xff\x43\x4b\x46\x49\x56\xff"

C_COMMAND_IDE_ITEM = b"\xff\x4b\x49\x54\x45\x4d\xff"


# 解析内容
def parsersBody(tmpretSet, deep=1):
    ret = []
    C_COMMAND_IDE_X = bytearray()
    switch = {
        "1": C_COMMAND_IDE_1,
        "2": C_COMMAND_IDE_2,
        "3": C_COMMAND_IDE_3,
        "4": C_COMMAND_IDE_4,
        "5": C_COMMAND_IDE_5,
    }
    if deep != 0:

        C_COMMAND_IDE_X = switch[str(deep)]

    # 是谁？ 1:list 2:item
    islist = 0

    # 准备读取flag
    rdyREAD = False
    rdyLEN = len(C_COMMAND_IDE_X)
    # 正在读取flag
    nowREAD = 0
    # list缓存
    tmpsublist = bytearray()

    # 查找区间
    for x in range(len(tmpretSet)):

        # 判断是否读取flag
        if rdyREAD:
            if rdyLEN > 1:
                rdyLEN -= 1
                continue
            else:
                rdyREAD = False
                rdyLEN = len(C_COMMAND_IDE_X)
                # 切换到读取
                nowREAD = 1

        # 判断是否是LIST
        if tmpretSet[x:x+7] == C_COMMAND_IDE_X and islist != 2:
            islist = 1
            if nowREAD == 0:
                rdyREAD = True
            elif nowREAD == 1:
                ret.append(parsersBody(tmpsublist, deep+1))
                tmpsublist = bytearray()
                nowREAD = 0
                islist = 0
        # 判断是否是ITEM
        elif tmpretSet[x:x+7] == C_COMMAND_IDE_ITEM and islist != 1:
            islist = 2
            if nowREAD == 0:
                rdyREAD = True
            elif nowREAD == 1:
                ret.append(tmpsublist.decode('utf-8', 'ignore'))
                nowREAD = 0
                tmpsublist = bytearray()
                islist = 0
        else:
            if nowREAD == 1:
                tmpsublist.append(tmpretSet[x])

    return ret


# 解析报文
def parsers(req):
    retCommand = ''
    retSet = []

    # 获得命令
    retCommand = req[0:req.find(C_COMMAND_IDE)].decode('utf-8', 'ignore')

    # 获得内容
    tmpretSet = req[req.find(C_COMMAND_IDE)+6:len(req)]
    retSet = parsersBody(tmpretSet)

    return retCommand, retSet
