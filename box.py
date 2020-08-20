w = 9
h = 5

for i in range(h):
    if not i or i == h-1:
        print('*'*w, end ='')
        print()
    else:
         print('*' + ' '*(w-2) + '*')