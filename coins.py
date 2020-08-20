number_of_coins = int(input('How many coins do you have? '))


#(f'You have {number_of_coins} coins? ')
question = 'yes'
while question == 'yes':
    number_of_coins += 1
    print(f'You have {number_of_coins} coins! ')
    question = input('Would you like another coin? ')

print('Goodbye!')
