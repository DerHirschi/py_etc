import socket
import threading


class ServerCfg(object):
    ip      = ''
    port    = 2222
    encrypt = True
    timeout = 30
    cach    = 256
    max_con = 1

    run_ind = True


class Server(threading.Thread):
    def __init__(self, cnfObj):
        threading.Thread.__init__(self)
        self.conf = cnfObj

    def run(self):
        _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            _s.bind((self.conf.ip, self.conf.port))
            _s.listen(self.conf.max_con)

            while self.conf.run_ind:
                client, address = _s.accept()
                client.settimeout(self.conf)

                #TODO ne runde schlafen
                #t = listen2client(client.timeout)
                #t.start()

        except:
            self.conf.run_ind = False



