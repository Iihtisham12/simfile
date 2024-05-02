print("My Second File For GitHub")
def sum(a,b):
    c = a + b
    return c

print(sum(28,98))

name = input("Enter Ur Name! \n")
try:
    if int(name) // int(name) == 1:
        print('Number is Not Allowed !!')
except:
    print(f"Hillo {name}")