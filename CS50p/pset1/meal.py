def main():
    plan = [
        {"meal": "breakfast time", "start hour": 7, "end hour": 8},
        {"meal": "lunch time", "start hour": 12, "end hour": 13},
        {"meal": "dinner time", "start hour": 18, "end hour": 19},
    ]

    time = input("What time is it? ").strip().lower()
    time = convert(time)

    for p in plan:
        if time >= float(p["start hour"]) and time <= float(p["end hour"]):
            print(p["meal"])


def convert(time):
    t = 0.0

    if time.rfind("a.m.") != -1:
        time = time.replace(" a.m.", "")
    if time.rfind("p.m.") != -1:
        time = time.replace(" p.m.", "")
        t = 12.0

    h, m = time.split(":")
    t = t + float(h) + (float(m) / 60)

    return t


if __name__ == "__main__":
    main()
