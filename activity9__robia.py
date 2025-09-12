
#list of student enrolled 
student1 = ["julius A Glamore", "kyle abokay", "bonbon gimo", "bembe aquino" ] 
print(student1)
name1 = input(" first name: ")
age = int(input(" age: "))
#list of coarse
coarse = ("Information system", "BSED", "BSARTS", "BSCRIM")
print(coarse)
major_in = input("major in: ")
average_grades = ""
if name1 == "julius":
   average_grades = 75
   student2 = {
    "name": name1,
    "age": age,
    "major in": major_in,
    "grades": average_grades
   }
   print(  student2, "\n You'v Passed", name1)

elif name1 == "kyle":
   average_grades = 89
   student2 = {
    "name": name1,
    "age": age,
    "major in": major_in,
    "grades": average_grades
   }
   print(  student2, "\n You'v Passed", name1)


elif name1 == "bonbon":
   average_grades= 90
   student2 = {
    "name": name1,
    "age": age,
    "major in": major_in,
    "grades": average_grades
}
   print(  student2, "\n You'v Passed", name1)


elif name1 == "bembe":
   average_grades = 99
   student2 = {
    "name": name1,
    "age": age,
    "major in": major_in,
    "grades": average_grades
   }
   print(  student2, "\n You'v Passed", name1)
