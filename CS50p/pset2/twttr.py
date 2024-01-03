vowels = ["a","A","e","E","i","I","o","O","u","U"]
input = input("INPUT: ").strip()
out = ""

for i in input:
   if i not in vowels:
       out = out + i

print(f"Output: {out}")
