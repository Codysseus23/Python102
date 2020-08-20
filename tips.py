bill = float(input('What was the bill amount? '))
service = input('Level of service? ')
party_split = int(input('Number of people in party? '))

if service == 'bad':
    tip_amount = bill * .10
    print(f'Tip amount: ${tip_amount}')
    print(f'Total bill is ${bill + tip_amount}')
    print(f'Cost per person is ${(bill + tip_amount) / party_split}')

elif service == 'fair':
    tip_amount = bill * .15
    print(f'Tip amount: ${tip_amount}')
    print(f'Total bill is ${bill + tip_amount}')
    print(f'Cost per person is ${(bill + tip_amount) / party_split}')

elif service == 'good':
    tip_amount = bill * .15
    print(f'Tip amount: ${tip_amount}')
    print(f'Total bill is ${bill + tip_amount}')
    print(f'Cost per person is ${(bill + tip_amount) / party_split}')

else:
    print('Please enter the bill total in a decimal form and put service as good, fair, or bad.')

