
from exec.command import C001, C002


def default(body):
    return 'None'


def doCommand(commondID, body):
    switch = {
        'C001': C001.main,
        'C002': C002.main,
        'C003': C001.main,
        'C004': C001.main,
        'C005': C001.main,
    }

    ret = switch.get(commondID, default)(body)
    return ret


def exec(socatclient, commondID, commondBody):

    rep = doCommand(commondID, commondBody)

    socatclient.send(rep.encode('utf-8'))

    return True, "任务执行完毕"
