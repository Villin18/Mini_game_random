import random


from game import logick_game


def main():
    print("="*30)
    print("Добро пожаловать в мини игру Угадайка")
    print("=" * 30)
    user_number = int(input("Введите число от 0 до 50: "))
    program_number = random.randint(0,50)
    logick_game(user_number,program_number)

if __name__ == "__main__":
    main()
