def timeConversion(s):
    sliced_s = s[:-2]
    meridian = s[-2:]
    colon = ":"
    hh, mm, ss = sliced_s.split(colon)
    if hh != '12':
        if meridian == 'PM':
            hh = str(int(hh)+12)
    if hh == '12':
        if meridian == 'AM':
            hh = '00'
        elif meridian == 'PM':
            hh = str(int(hh)+0)
    military_time = colon.join([hh, mm, ss])
    return military_time
print(timeConversion('07:05:45PM'))
