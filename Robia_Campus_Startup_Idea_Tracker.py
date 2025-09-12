# Campus Startup Idea Tracker

students = []

# collect data for 5 students
for i in range(5):
    print("Student", i+1)
    name = input("Enter name: ")
    idea = input("Enter startup idea: ")
    market = input("Enter market (Youth / Professionals / Local Community): ")
    cost = float(input("Enter estimated cost: "))
    revenue = float(input("Enter expected monthly revenue: "))

    student = {"name": name, "idea": idea, "market": market, "cost": cost, "revenue": revenue}
    students.append(student)

# check viability for each student
print("--- Business Viability ---")
for s in students:
    if s["revenue"] >= 2 * s["cost"]:
        print(s["name"], ":", "High Viability")
    elif s["revenue"] >= s["cost"]:
        print(s["name"], ":", "Moderate Viability")
    else:
        print(s["name"], ":", "Low Viability - Needs Revision")

# count markets
youth = 0
prof = 0
local = 0
for s in students:
    if s["market"] == "Youth":
        youth += 1
    elif s["market"] == "Professionals":
        prof += 1
    elif s["market"] == "Local Community":
        local += 1

print("Market Summary")
print("Youth:", youth)
print("Professionals:", prof)
print("Local Community:", local)

# average cost
total_cost = 0
for s in students:
    total_cost += s["cost"]
avg_cost = total_cost / len(students)
print("Average Cost:", avg_cost)

# feedback
print("--- Feedback ---")
for s in students:
    if s["revenue"] >= 2 * s["cost"]:
        print(s["name"], "your idea shows strong potential—consider pitching to investors!")
    elif s["revenue"] >= s["cost"]:
        print(s["name"], "your idea is promising—refine your business model.")
    else:
        print(s["name"], "revisit your cost structure and revenue strategy.")

# search student
search_name = input("Enter student name to search (case-sensitive): ")
found = False
for s in students:
    if s["name"] == search_name:
        print("Startup Record")
        print("Name:", s["name"])
        print("Idea:", s["idea"])
        print("Market:", s["market"])
        print("Cost:", s["cost"])
        print("Revenue:", s["revenue"])
        found = True
if not found:
    print("Startup record not found.")

# weekly projection for first student
print("Weekly Revenue Projection for", students[0]["name"])
daily = []
for i in range(7):
    r = float(input("Day " + str(i+1) + " revenue: "))
    daily.append(r)

avg_rev = sum(daily) / 7
print("Average daily revenue:", avg_rev)

if avg_rev > 5000:
    print("Strong revenue forecast—consider scaling up!")
elif avg_rev >= 2000 and avg_rev <= 5000:
    print("Moderate forecast—continue refining your strategy.")
else:
    print("Low forecast—explore ways to boost market appeal.")