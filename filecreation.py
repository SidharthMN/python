store_data = open("newfile.txt","w")
store_data.write("Welcome to Python Programming")
print(store_data)
store_data.close()

'''read_data = open("newfile.txt","r")
print(read_data.read())
read_data.close()'''

append_data = open("newfile.txt","a")
append_data.write("\nPython is a interpreted language")
print(append_data)
append_data.close()

read_data = open("newfile.txt","r")
print(read_data.read())
read_data.close()
