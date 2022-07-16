for number in range(1,11):
    print(number)

list = ["Cameron","Kayla","Janai","Jiana"]

for i in list:
    print(i)

vowels = 0
consonants = 0
for letters in "asdkjfhvbasgknadfgldbldbvlkjsdvnvdbv":
    if letters.lower in ("aeiou"):
        vowels = vowels + 1
    else:
         consonants = consonants + 1
print("There are {} vowels and {} consontants".format(vowels,consonants))