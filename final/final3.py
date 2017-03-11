trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    n = int(us_num)
    if n <= 10:
        return trans[us_num]
    elif n <= 19:
        return 'shi ' + trans[us_num[1]]
    elif int(us_num[1]) == 0:
        return trans[us_num[0]] + ' shi'
    else:
        return trans[us_num[0]] + ' shi ' + trans[us_num[1]]