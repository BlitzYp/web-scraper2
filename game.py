def handle_game(data: tuple, hint: str):
    print(data)
    print("Welcome to my quote testing game! Do you have what it takes to beat this game?")
    tries: int = 5
    while tries > 0:
        print(data[0])
        user_res: str = str(input("Who is the author of this quote?: "))
        if user_res.lower() in data[1].lower():
            return f'You are correct! The author is {data[1]}'
        else:
            tries -= 1
            print(f'{user_res}: is not correct! Try again!')
            print(f"Hint: {hint}")
            continue
    else:
        return f'Ahhhh the answer was: {data[1]}...Do you want to play again?: '
