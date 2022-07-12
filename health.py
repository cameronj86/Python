import random
health = 50
difficulty = 1
maxhealth = 100 - health
potionHealth = random.randint(25,maxhealth)/difficulty
health = int(potionHealth) + health


print(health)