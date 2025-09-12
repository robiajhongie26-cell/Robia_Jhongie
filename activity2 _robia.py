
# Guess the right number

num = int(input("input random number: "))

while True: 
   
    if num >= 1 and num <= 23:
        print ("to low")
        break
    elif num == 24 :
         print( "you won ", num)
         break
    elif num >= 25 and num <=100 :
        print("too high ", num)
        break
        



