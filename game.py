def logick_game(user_number, program_number):
    counter = 1

    while True:
        if user_number > program_number:
            print('Ваше число больше')
            user_number = int(input("Попробуйте еще раз: "))
            counter += 1
        elif user_number < program_number:
            print("Ваше число меньше")
            user_number = int(input("Попробуйте еще раз: "))
            counter += 1
        else:
            print(f"Поздравляем! Вы угадали число {program_number} за {counter} попыток")
            break