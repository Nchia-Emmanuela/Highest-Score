scores = input("Enter students scores:\n").split()
print(scores)
int_max = 0
for scr in scores:
    score = int(scr)
    if score > int_max:
        int_max = score
print(f"the highest score in the class is: {int_max}")
