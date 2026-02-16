import random

MAX_NUM = 10
MIN_NUM = 1
MAX_GUESS_COUNT = 3


def generate_random_number():
    return random.randint(MIN_NUM, MAX_NUM)


def get_user_input():
    print(f"== Your number should between {MIN_NUM} - {MAX_NUM} ==")

    while True:
        try:
            user_input = int(input("Guess Number:"))
        except ValueError:
            print("Number is not valid!")
        else:
            return user_input


def check_guess_number(user_input, random_num):
    return user_input == random_num


if __name__ == "__main__":
    random_num = generate_random_number()

    while MAX_GUESS_COUNT > 0:
        user_input = get_user_input()
        if check_guess_number(user_input, random_num):
            print("you have guess successfully!")
            break

        MAX_GUESS_COUNT -= 1

        print("guess left:", MAX_GUESS_COUNT)
    else:
        print("you couldn't guess number,and ran of guess!")
