even_numbers = [x for x in range(1,100) if x <50]
print(even_numbers)

#Don't quite get the string usage yet but I'll figure it out
speech = ["Well","I", "guess","I'm","getting","the","hang","of","Python"]
speechBreakdown = [[s.upper(),s.lower(),len(s)] for s in speech ]