Films = {
     "Finding Dory":{"MPAARating":"G","Seats Available":26}
    ,"Tomorrow Never Dies":{"MPAARating":"R","Seats Available":12}
    ,"Tenet":{"MPAARating":"R","Seats Available":46}
    ,"Jumanji":{"MPAARating":"G","Seats Available":4}
    ,"Knives Out":{"MPAARating":"PG 13","Seats Available":100}
    ,"Spiderman: No Way Out":{"MPAARating":"PG 13","Seats Available":4}
    ,"Venom":{"MPAARating":"R","Seats Available":22}
}

while True:
    filmChoice = input("What film would you like to see: ").strip().title()
    if filmChoice in Films:
        age = input("We have that film available. Can I confirm your age before we go further? ")
        age = int(age)
        if age > 17:
            elig = True 
        elif age >= 13 and Films[filmChoice]["MPAARating"] in ("G","PG 13"):
            elig = True 
        elif  Films[filmChoice]["MPAARating"] == ("G"):
            elig = True 
        else: 
            elig = False
            print("I'm sorry fam but you're too young to see this movie")
    if elig:
        tixNum = int(input("How many tickets do you need fam?: ").strip())
        while tixNum > Films[filmChoice]["Seats Available"]:
            if  tixNum <= Films[filmChoice]["Seats Available"]:
                print("Yes, here are {} tickets for the next showing of {}. Enjoy the show!".format(tixNum,filmChoice))
            else: 
                print("Sorry fam, we don't have that many left. Try again") 
                break
    else: print("I'm sorry but we aren't showing {} here unfortunately. Try another film!".format(filmChoice))

