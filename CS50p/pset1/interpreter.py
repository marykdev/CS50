a,y,c = input("Expression: ").strip().split(" ")

x = float(a)
z = float(c)

if y == "+":
    print(f"{(x + z):.1f}")
elif y == "-":
    print(f"{(x - z):.1f}")
elif y == "*":
    print(f"{(x * z):.1f}")
elif y == "/":
    print(f"{(x / z):.1f}")