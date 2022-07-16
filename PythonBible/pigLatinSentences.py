
original = input("Type in a sentence: ").strip().lower()

words = original.split()
vowel_list = "aeiou"
# original = list(original)
# print(original)

new_words = []

for word in words:        
    if word[0] not in vowel_list:
        vowel_pos = 0
        for letter in word:
            if letter not in vowel_list:
                vowel_pos = vowel_pos + 1
            else:
                break # this breaks us out of the loop 
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        pigLatin = the_rest + cons + "ay"
        # # pigLatinWord2 =word[1:]
        # word2 = pigLatinWord2 + word[0].capitalize()
        # pigLatin = "{}ay".format(word)
        new_words.append(pigLatin)
    else:
        pigLatin = "{}yay".format(word)
        new_words.append(pigLatin)
new_words = " ".join(new_words).capitalize()
print(new_words)