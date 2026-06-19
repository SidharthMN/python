'''
store_data = open("newfile.txt","w")
store_data.write("Welcome to Python Programming")
print(store_data)
store_data.close()

read_data = open("newfile.txt","r")
print(read_data.read())
read_data.close()

append_data = open("newfile.txt","a")
append_data.write("\nPython is a interpreted language")
print(append_data)
append_data.close()

read_data = open("newfile.txt","r")
print(read_data.read())
read_data.close()
'''
'''
#Using Context Manager
with open("newfile.txt","r") as f:
   print("Current Position : ",f.tell())
   f.read(6)
   print("After read position : ",f.tell())
   f.seek(4)
   print("After Seek : ",f.tell())
   print(f.read())

'''
'''
with open ("car.jpg","rb") as data:
    image_read=data.read()
    print(image_read)

#tryout pip install pillow and use its functions

tech = open("delete_file.txt","x")
print(tech)
tech.close()
'''
'''
filepath = "delete_file.txt"
import os
if os.path.exists(filepath):
    os.remove(filepath)
    print(f"{filepath} deleted successfully")
else:
    print(f"{filepath} doesn't exist")
'''
'''
print("Serialisation and Deserialisation")
import pickle 

data = {
    "students": ["Aria","Rajesh","Vimal"],
    "marks" : (78,87,69),
    "subjects" : {"Malayalam","Maths","English"}
    }

'''

'''
#Serilaisation - Saving data to file

with open("user_details.pkl","wb") as f:
    pickle.dump(data,f)
print("Data is serialised to user details ",data)

with open("user_details.pkl","rb") as f:
    loaded_data = pickle.load(f)
print("Data is deserialised ",loaded_data)

dump_data = pickle.dumps(data)
print("Data is serialised to bytes :",dump_data)

load_data = pickle.loads(dump_data)
print("Data is sserialised to objects : ",load_data)
#tryout json module also
'''
