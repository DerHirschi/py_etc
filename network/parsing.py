from etc.var import array2sting
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
        flag     = ''
        st_split = ''

        def server(self, dat):
            print 'server {}'.format(array2sting(dat[1:], ' '))

        def client(self, dat):
            print 'client {}'.format(array2sting(dat, self.st_split))
            print 'st_split {}'.format(self.st_split)
            return self.flag + array2sting(dat, self.st_split)

    def __init__(self, data):
        self.flaglen = len(self.flag)
        if type(data) == str:
            self.server(data)
        elif type(data) == list:
            self.client(data)

    def server(self, dt):

        if dt[:self.flaglen] != self.flag:
            return False
        else:
            _t = dt[self.flaglen:]
            self.pac = _t.split(self.st_split)
            _mt = self.pac_type(int(_t[0]))
            if _mt:
                _mt.server(self.pac)
                return True
            else:
                return False

    def client(self, da):
        self.pac = da
        _mt = self.pac_type(int(da[0]))
        if _mt:
            print _mt.client(self.pac)
            return _mt.client(self.pac)
        else:
            return ''
        #return self.flag + data

    def pac_type(self, typ):

        _di = {
            0: self.defaultPacket(),
        }
        if typ in _di:
            _f = _di[typ]
            _f.st_split = self.st_split
            _f.flag = self.flag
            return _f


def parse_pack(packet):
    return PasingTab(packet).res


PasingTab('SFL0%sdgfsgagrgrg%1111111111111%sagg')
PasingTab('SFL0%sdgfsgagrgrg 0000000000000')
PasingTab([0,543,'46346',346,'fg', '1111111111111'])
PasingTab([0,543,'46346',346,'fg', '0000000000000'])

