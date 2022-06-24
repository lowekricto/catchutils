import logging

# 系统运行间隔 默认：300s
SYS_TIME_RUNNING_CIRCLE = 300
# 系统故障重启间隔 默认：60s
SYS_TIME_RESTART_CIRCLE = 60

# 主机地址
DB_HOST = "127.0.0.1"
# DB_HOST = "192.168.200.143"
# 连接用户名
DB_USER = "root"
# 密码
DB_PASSWORD = "ITcw15eQ65"
# 数据库名
DB_NAME = "ics_sec"
# 连接端口号
DB_PORT = 3306

# LOG打印输出位置
# LOG_NAME = '/home/log/socat.log'
LOG_NAME = 'socat.log'
# LOG打印输出级别
# LOG_LEVEL = logging.WARN
LOG_LEVEL = logging.INFO
