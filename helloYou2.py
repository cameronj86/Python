#Name
Name = input("What is your name?: ")
print("Hello " + Name)
#Age
Age = input("How old are you " + Name + "?: ")
#City
City = input(Age + " is getting up there. Where do you live " + Name + "?: ")

#What they enjoy
Response = input("Dope! I've heard nice things about " + City + ". What do you enjoy in " + City + ", " + Name + "?: ")
#Create output text
ResponseText = "OK, so I just want to make sure I have everything right... You are a {} year old named {} and you currently reside in {}?. Also, you love {}"
OuputText = ResponseText.format(Age,Name,City,Response)
print(Name)
#Print Output to screen
print(OuputText)