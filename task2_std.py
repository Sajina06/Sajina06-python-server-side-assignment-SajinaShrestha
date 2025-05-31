#Create a program that takes a list of student names and stores them in a file .Then read the file and display the contents.

n= int(input("enter number of students"))
with open ("std.txt","w") as f:
    for i in range(n):
        name=input(f"enter a name of students")
        f.write("{:<15}\n".format(name))

with open ("std.txt","r") as f:
    
    print("sucess")
       