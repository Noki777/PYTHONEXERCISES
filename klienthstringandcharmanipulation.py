#klienth engyo

name = input ("enter your name:")
new_name = ""
my_name = "noki"
#kapag may kaparehas na letter sa name magskip at mag output ng letter na wala sa name
print("noki")
print
for letter in name:
 if letter not in my_name:
    new_name += letter
    print ("A name is created :", new_name)

print("your new name is :", new_name)
print ("")
input ("enter to exit")