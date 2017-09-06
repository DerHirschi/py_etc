# Author DerHirschi
import os

# 1 Daten ( egal welcher daten typ)
# 2 Dateiname
# 3 (opt)Neue Datei erstell wenn Datei schon existiert - default True
# 4 (opt)Pfad - default Projekt Rootverzeichniss
def write(data, f_ile, new_file=True, path=''):
    def _add_nl(st_r):
        if type(st_r) != str:
            st_r = str(st_r)
        if bool(st_r.find('\n') + 1):
            return st_r
        else:
            return st_r + '\n'

    _f_name = path + f_ile
    if new_file:
        _n = 1
        _i = (_f_name.find('.'))
        _e = _f_name[_i:]
        while os.path.exists(_f_name):
            _f_name = _f_name[:_i] + '_{}'.format(_n) + _e
            _n += 1

    _f = open(_f_name, 'a')

    if type(data) == str:
        _f.write(_add_nl(data))
    elif type(data) == list or type(data) == tuple:
        for i in range(len(data)):
            _f.write(_add_nl(data[i]))
    elif type(data) != dict:
        _f.write(_add_nl(data))

    _f.close()

# Test it !!!
if __name__ == '__main__':
    write('jeahhh','test.txt')
    write(3,'test.txt')
    write((3, 'afafa'),'test.txt', False)
    write([3,
           False,
           'sdgfa',
           'afafa',
           'sdgfa',
           'afafa',
           'sdgfa',
           'afafa',
           'sdgfa',
           'afafa',
           'sdgfa',
           'afafa',
           'sdgfa',
           'afafa',
           'sdgfa',
           'afafa',
           'sdgfa',
           'afafa'
          ],'test.txt', False)

