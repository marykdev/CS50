while True:
    tank = input("Fraction: ").strip()

    try:
        up, down = tank.split("/",1)

        if up.isdigit() and down.isdigit() and int(up) <= int(down) and int(down) !=0:
            fuel = int(up) / int(down) * 100

            if fuel >= 99:
                print("F")
                break
            elif fuel <= 1:
                print("E")
                break
            else:
                print(f"{fuel:.0f}%")
                break
    except (ValueError,ZeroDivisionError):
        pass
    else:
        pass
