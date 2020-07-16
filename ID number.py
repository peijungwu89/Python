import re

# Determine the correct ID number

area = '0123456789ABCDEFGHJKLMNPQRSTUVXYWZIO'

inputid = 'B123456789'

total = 0

if re.match('^[A-Z]{1}(1|2)\\d{8}$',inputid):
    
    for i in range(9):
        index = area.index(inputid[i])
        if index >= 10:
            total += index // 10 * 1
            total += index % 10 * 9
        else:
            total += index * (9-i)    
    print('total=', total)   
    if (10 - (total % 10)) == int(inputid[9]):
        print(inputid, 'Correct')
    else:
        print(inputid, 'Wrong')

else:
    print('Format error')
