def make_choice(x, y, field):
    for i in range(0, x):
        if field[i][y] not in [0, -1, 1]:
            return "fire_left"


if __name__ == "__main__":
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(make_choice(0, 0, field))
