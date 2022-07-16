
pigLatinWord = input("Choose a word: ").strip().lower()

if pigLatinWord[0] not in "aeiou":
    pigLatinWord2 = pigLatinWord[1:]
    pigLatinWord = pigLatinWord2 + pigLatinWord[0].capitalize()
    pigLatin = "{}ay".format(pigLatinWord)
else:
    pigLatin = "{}yay".format(pigLatinWord)
print(pigLatin)