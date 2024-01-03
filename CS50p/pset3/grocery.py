grocery = {}

while True:
    try:
        item = input().strip().upper()

        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    except(EOFError,KeyError):
        for key in sorted(grocery.keys()):
            print(f"{grocery[key]} {key}")
        quit()