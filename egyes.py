
def Base2to10(szam,base):

    power = 1
    num = 0

    rev_str_num = str(szam)[::-1]
    for i in map(str,rev_str_num):
        num += int(i) * power
        power = power * base
    str_num = str(num)
    return str_num




def base10to2(num, base):

    converted_string = ""
    currentnum = int(num)
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    result = int(converted_string)
    return result




