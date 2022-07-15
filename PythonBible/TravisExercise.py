known_users = ["Alice", "Bob", "Claire","Dan","Emma","Fred","Georgie", "Harry" ]

while True:
    print("Hi! My Name is Travis")
    name = input("What is your name?: ").strip().title()
    
    if name in known_users:
        print("Hello {}! Nice seeing you again!".format(name))
        remove = input("Would you like to be removed from the list {} (y/n)?".format(name)).title().strip().lower()

        if remove  == 'Y':
            known_users.remove(name)
    else:
        print("You looking real unfamiliar {}...".format(name))
        addme = input("Would you like to get added to our group {}? ".format(name)).title().strip().lower()
        if addme == 'y':
            known_users.append(name)
            print(known_users)
        elif addme == 'n':
            print("Alright bet. Say less fam")
