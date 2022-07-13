# from socket import MsgFlag
# from unicodedata import name


# Get email
email = input("What's your email address? ")

# slice out username
username = email[0:email.index("@")].strip()
username = username.title()

# slice domain name
emailDomain = email[email.index("@")+1:] #Ziyad showed me about the index + 1 to move one addtl character over
# emailDomain = emailDomain[1::] #no longer need this code after the prior workaround
emailDomain = emailDomain[:emailDomain.index(".com"):]
emailDomain = emailDomain.title()

# format Msg
# output = "I believe your username is {} and your email address is with {}"
# print(output.format(username,emailDomain)) my initial sloppy workaround

#Much cleaner way that formats/references the string itself
output = "I believe your username is {} and your email address is with {}".format(username,emailDomain)
print(output)

# Display output msg 