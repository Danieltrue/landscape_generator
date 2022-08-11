import random
from noise import pnoise2
from termcolor import colored


def generate_landspace(cols=10,rows=10,noise_level=10):

    data = ["🌱","🌲","🌊","🌵","🌴","🌾"]
    seed = random.randint(0,100)
    land = ""


    print(colored(f'Generating a landspace which is {cols} by {rows}',"red"))

    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row / rows, col / cols, base=seed, octaves=5)
            n *= noise_level
            n = round(n)
            n = n % len(data)

            land += data[n]
        land += "\n"
        return land


    print('Finished generating landspace')


def answer_number(question):
    answer = input(question)

    if answer.isnumeric():
        return int(answer)
    else:
        print(f"[Error]: Insert a number")
        quit()
if __name__ == '__main__':
    cols = answer_number('How many cols? ')
    rows = answer_number('How many rows? ')

    land = generate_landspace(cols, rows)

    print(land)
