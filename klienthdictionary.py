print ("welcome")

Nokilist =[]

add= input("ADD SOMETHING INTO THE LIST YES OR NO?:")

while add.lower() == "y":
    item = input("Enter your item to the lisT:")
    Nokilist.append(item)
    add = input("Want to add your Shopping list ? YES OR NO:")

print(">")
print("Here is your alphabetized List")
Nokilist.sort()
for listitem in Nokilist:
 print(">"+listitem)



