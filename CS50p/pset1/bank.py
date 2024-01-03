i = input("Greeting: ").strip().lower()

if i.startswith("hello"):
    o = 0
elif i.startswith("h"):
    o = 20
else:
    o = 100

print(f"${o}")