#klienth

print ("BODY MASS INDEX")

userw = float ( input("Please enter your weight in kg:"))
userh = float ( input("Please enter your height in inches:"))

userbmi =(userw * 703) / (userh**2)

print()

if userbmi <18.5:
    print ("A person with a BMI of" + format(userbmi) + "is underweight")
elif userbmi <26:
    print("A person with BMI of " + format (userbmi) + "has an normal weight")

else:
    print ("a person with bmi of" + format (userbmi)+ "is over weight")
