# TODO Checksumm https://stackoverflow.com/questions/3949726/calculate-ip-checksum-in-python
class PasingTab:
    # CFG
    flag        = 'SFL'
    st_split    = '%'
    # vars
    res         = ''
    pac         = []
    # Fuck .. i think i am loop my self

    class defaultPacket:
        def __init__(self, data):
            self.data = data

        def server(self):
            print 'server {}'.format(self.data)

        def client(self):
            print 'client {}'.format(self.data)

    def __init__(self, data):
        self.flaglen = len(self.flag)
        if type(data) == str:
            self.server(data)
        elif type(data) == list:
            self.client(data)

    def server(self, data):

        if data[:self.flaglen] != self.flag:
            return []
        else:
            _t = data[self.flaglen:]
            self.pac = _t.split(self.st_split)
            _mt = self.pac_type(int(_t[0]))
            _mt.server()

    def client(self, data):
        self.pac = data
        _mt = self.pac_type(int(data[0]))
        _mt.client()
        #return self.flag + data

    def pac_type(self, typ, server=True):
        return {
          0: self.defaultPacket(self.pac),
        }[typ]


def parse_pack(packet):
    return PasingTab(packet).res


PasingTab('SFL0%sdgfsgagrgrg')
PasingTab([0,543,'46346',346,'fg'])

