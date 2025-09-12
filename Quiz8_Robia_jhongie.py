# validating student access to the library base on ID
# and outstanding funds



student_id = input("enter student ID(numeric)  ")

 
 
student_id= int(student_id)

fines = float(input("enteramount of standing fines: "))
if fines < 0:
    raise ValueError("outstanding fines connot be negative")

if student_id > 0 and fines == 0:
    print("Access Granted ")
else:
    print("Access Denied")
    
