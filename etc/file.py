# Author DerHirschi
from var import count_filename


# 1 Daten ( egal welcher daten typ)
# 2 Dateiname
# 3 (opt)Neue Datei erstell wenn Datei schon existiert - default True
# 4 (opt)Pfad - default Projekt Rootverzeichniss
# 5 (opt)Option Datum oder Zeit im Dateinamen + Count
#   'count'/'date'/'time'

def write(data, f_ile, new_file=True, path='', opt='count'):
    def _add_nl(st_r):
        if type(st_r) != str:
            st_r = str(st_r)
        if bool(st_r.find('\n') + 1):
            return st_r
        else:
            return st_r + '\n'

    _f_name = path + f_ile
    if new_file:
        _f_name = count_filename(_f_name, opt)

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

    write('jeahhh','test.txt', True, '',)
    write('jeahhh','test.txt', True, '', 'date')
    write('jeahhh','test.txt', True, '', 'time')
    write('jeahhh','test.txt', True, '', 'time')
