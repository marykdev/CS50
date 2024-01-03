def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    numcheck = 0
    validated = ""

    if len(s) >= 2 and len(s) <= 6:
        if s[0:1].isalpha():
            for l in s:
                if l.isalpha() or l.isnumeric():
                    if l.isnumeric() and numcheck == 0 and l != "0":
                        numcheck += 1
                        validated += l
                    elif l.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += l
                    elif l.isalpha() and numcheck == 0:
                        validated += l

    if validated == s:
        return True
    else:
        return False

main()