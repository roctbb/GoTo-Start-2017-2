temperature = int(input('введите температуру:'))
is_raining = input('Идет ли дождь? (да/нет)')

if temperature > 30:
    print("Слишком жарко :(")
elif temperature > 20 and is_raining == 'нет':
    print("ЧТо как сыч сидишь!")
else:
    print('Го в доту я создал!')
