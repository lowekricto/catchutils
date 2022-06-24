from socat import SOCAT
import threading


def main():

    t1 = threading.Thread(target=SOCAT.socat)
    t1.setName('SOCAT-MAIN')
    t1.start()


main()
