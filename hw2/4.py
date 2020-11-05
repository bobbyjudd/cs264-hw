def delta(a,b,c,d,e):
    return ((not d or not e or b) and
        (not b or e or not a) and
        (not d or c or not b) and
        (not b or c or e))

def get_bool_char(value):
    if value:
        return 'T'
    return 'F'

vals = [True, False]
t_cnt, f_cnt = 0, 0
for a in vals:
    for b in vals:
        for c in vals:
            for d in vals:
                for e in vals:
                    delt = delta(a,b,c,d,e)
                    if delt:
                        t_cnt += 1
                    else:
                        f_cnt += 1
                    print('{}&{}&{}&{}&{}&{} \\\\'.format(get_bool_char(a),
                        get_bool_char(b),
                        get_bool_char(c),
                        get_bool_char(d),
                        get_bool_char(e),
                        delt))
print('True Count {}\nFalse Count {}'.format(t_cnt, f_cnt))
