import socket
import threading

from etc.log import log, var_hint


class ServerCfg(object):
    ip = ''
    port = 2222
    encrypt = True
    timeout = 45
    cach = 256
    max_con = 2

    run_ind = True
    sockobj = None


class Server(threading.Thread):
    def __init__(self, cnf_obj):
        threading.Thread.__init__(self)
        self.conf = cnf_obj
        self.cli = []

    def run(self):
        self.conf.sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conf.sockobj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        log('Try to start on IP: {} , Port: {}'.format(self.conf.ip, self.conf.port), 10)

        try:
            self.conf.sockobj.bind((self.conf.ip, self.conf.port))
            self.conf.sockobj.listen(self.conf.max_con)

            log('started on IP: {} , Port: {}'.format(self.conf.ip, self.conf.port), 10)
            log('Waiting for incoming connection ...', 10)

            while self.conf.run_ind:
                client, address = self.conf.sockobj.accept()
                log('Connection established with {}'.format(address[0]), 10)
                client.settimeout(self.conf.timeout)
                self.cli.append(client)
                threading.Thread(target=self.listen2client, args=(client, address)).start()

        except:
            if self.conf.run_ind:
                log('Cant start Server IP: {} , Port: {}'.format(self.conf.ip, self.conf.port), 11)
                self.conf.run_ind = False
            else:
                log('Server {} , {} stoped ...'.format(self.conf.ip, self.conf.port), 10)
                _n = 1
                while len(self.cli) > 0:
                    self.cli[0].shutdown(0)
                    log('Force disconnect Client #{}'.format(_n), 10)
                    _n += 1

    def listen2client(self, clt, fuck_dummy):
        while self.conf.run_ind:
            try:
                data = clt.recv(self.conf.cach)
                if data and self.conf.run_ind:
                    log('in_Data: {}'.format(data), 19)
                    log('Size: {} Bytes'.format(len(data)), 19)

                else:
                    break
            except:
                break
        self.cli.remove(clt)
        clt.close()

