students = {
     "Male":["Tom","Ryan","Jack","Ross","Marcus"]
    ,"Female":["Rachel","Leslie","Michelle","Dee","Ellen"]
}

for key in students.keys():    #(key = males loop then females) studentes.keys = drilled down values (individual names)
    for name in students[key]: #for every drill down value (now called 'name')
        if "a" in name:        # if 'a' is in the drilled down value
            print(name)        #print the name
