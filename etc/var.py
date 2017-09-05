import time


def array2sting(data, cut_flag=','):
    _temp = ''
    for i in range(len(data)):
        if type(data[i]) != str:
            _temp = _temp + str(data[i]) + cut_flag
        else:
            _temp = _temp + data[i] + cut_flag
    return _temp[:(len(_temp) - 1)]


def string2array(data, cut_flag=' ', cut_blank=True, conv2int=True):
    _data = data.split(cut_flag)
    _temp = []
    for i in range(len(_data)):
        if _data[i] == '' and cut_blank:
            pass
        else:
            try:
                if conv2int:
                    _temp = _temp + [int(_data[i])]
                else:
                    _temp = _temp + [_data[i]]
            except:
                _temp = _temp + [_data[i]]
    return _temp


def get_time(opt='all', string=False):
    def _monat(lst, trig):
        if not trig:
            return lst
        else:
            return {
                'Jan': 1,
                'Feb': 2,
                'Mar': 3,
                'Apr': 4,
                'May': 5,
                'Jun': 6,
                'Jul': 7,
                'Aug': 8,
                'Sep': 9,
                'Oct': 10,
                'Nov': 11,
                'Dec': 12,
            }[lst]

    def _conv_all():
        if string:
            return array2sting(string2array(time.ctime(), ' '), '-')
        else:
            return string2array(time.ctime(), ' ')

    _day_string = {
        True: 0,
        False: 2,
    }

    return {
        # 'all': string2array(time.ctime(), ' '),
        'all': _conv_all(),
        'year': string2array(time.ctime(), ' ', True, not string)[4],
        'mon': _monat(string2array(time.ctime(), ' ')[1], not string),
        'day': string2array(time.ctime(), ' ')[_day_string[string]],
        'time': string2array(time.ctime(), ' ')[3],
        'h': string2array(str(string2array(time.ctime(), ' ')[3]), ':', True, not string)[0],
        'min': string2array(str(string2array(time.ctime(), ' ')[3]), ':', True, not string)[1],
        'sek': string2array(str(string2array(time.ctime(), ' ')[3]), ':', True, not string)[2],
    }[opt]


def date2filename(f_name, time_form='date', cut_flag='_'):
    _i = f_name.find('.')
    _temp = f_name[_i:]
    return f_name[:_i] + '_' + build_date_st(time_form, cut_flag) + _temp


def build_date_st(t_f, c_f):
    if t_f == 'all':
        return build_date_st('date', c_f) + c_f + build_date_st('time', c_f)
    else:
        return {
            'date': str(get_time('year')) + c_f + str(get_time('mon')) + c_f + str(get_time('day')),
            'time': str(get_time('h')) + c_f + str(get_time('min')) + c_f + str(get_time('sek')),
        }[t_f]

