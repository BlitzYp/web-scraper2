import random


def handle_game(data: tuple, date: str, location: str):
    print("Hello there! Today I will test you knowledge about quotes!")
    tries: int = 5
    while tries > 0:
        print(data[0])
        user_res: str = str(input("Who is the author of this quote?: "))
        if user_res.lower() in data[1].lower():
            return f'You are correct! The author is {data[1]}'
        else:
            tries -= 1
            print(f'{user_res}: is not correct! Try again!')
            print("Hint")
            print(random.choice([date, location]))
            continue
    return f'Ahhhh the answer was: {data[1]}...Do you want to play again?: '
