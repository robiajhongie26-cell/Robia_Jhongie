start = int(input("enter starting number: "))
stop = int(input("enter end number:  "))
for number in range ( start, stop + 1):

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")






