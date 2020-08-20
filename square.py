side = int(input("Please Enter Size of a Square  : "))
i = 0
print("Square Star Pattern") 

while(i < side):
    star = 0
    while(star < side):      
        star = star + 1
        print('*', end = '  ')
    i = i + 1
    print('')