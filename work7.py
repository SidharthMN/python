print("Student Club Manager")
username = input("Enter username : ") 
low = username.lower()
up = username.upper()
title = username.title()
replace = username.replace("a","z")
find = username.find("a")
count = username.count("a")
start = username.startswith("A")
end = username.endswith("h")
split = username.split()
strip = username.strip()

print("Lower is : ",low)
print("Upper is : ",up)
print("Title is : ",title)
print("Replace is : ",replace)
print("Find is : ",find)
print("Count is : ",count)
print("Start with is : ",start)
print("Ends with is : ",end)
print("Split is : ",split)
print("Strip is : ",strip)

#Club Activities

club_activities = ("Coding","Quiz","Workshop","Hackathon","Quiz")

print("First Activity : ",club_activities[0])
print("Last Activity : ",club_activities[4])
print("Activities : ",club_activities[:])
print("Occurence of Quiz : ",club_activities.count("Quiz"))
print("Index of Workshop : ",club_activities.index("Workshop"))

#Club Mmebers

club_members = ["Sidharth","Mia","Gowtham","Mia"]
club_members.append("Pamman")
club_members.extend(["Sidxoid","Zentistu"])
club_members.insert(2,"Karupp")
club_members.remove("Sidharth")
pop_member = club_members.pop()
 
club_members.sort()
club_members.reverse()
club_members.index("Gowtham")
club_members.count("Mia")

print("Club Members : ",club_members)
print("Pop Members : ",pop_member)

#Club Event Participation

students = {"Abhijith","Akshay","Abhiram","Abhishek","Arjun"}
students.add("Sashi")
print("Add a participate : ",students)
students.update(["Sukhu","Shibu"])
print("Multiple Participant : ",students)
students.remove("Sashi")
print("Remove Student : ",students)
students.discard("Abhishek")
print("Discard Member : ",students)

student1 = {"a","b","c","d"}
student2 = {"c","d","r","s"}

union = student1.union(student2)
intersect = student1.intersection(student2)
difference = student1.difference(student2)
symmetric_difference = student1.symmetric_difference(student2)


print("Union of two sets : ",union)
print("Intersect of two sets : ",intersect)
print("Difference of two sets : ",difference)
print("Symmetric Difference of two sets : ",symmetric_difference)