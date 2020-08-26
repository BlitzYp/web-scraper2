import random
import termcolor


def handle_game(data: tuple, date: str, location: str):
    print(termcolor.colored(
        "Hello there! Today I will test you knowledge about quotes!", 'green'))
    tries: int = 5
    while tries > 0:
        print(termcolor.colored(data[0], 'yellow'))
        user_res: str = str(input("Who is the author of this quote?: "))
        if user_res.lower() in data[1].lower() and user_res:
            return termcolor.colored(f'You are correct! The author is {data[1]}', 'green')
        else:
            tries -= 1
            print(termcolor.colored(
                f'{user_res}: is not correct! Try again!', 'red'))
            print("Hint: ", termcolor.colored(
                random.choice([date, location]), 'green'))
            continue
    return termcolor.colored(f'Ahhhh the answer was: {data[1]}......', 'red')
