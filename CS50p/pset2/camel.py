camel = input("camelCase: ").strip()

snake = ""
for c in camel:
    if c.isupper():
        snake += "_"
        snake += c.lower()
    else:
        snake += c

print(f"snake_case: {snake}")