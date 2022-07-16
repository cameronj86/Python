import random

babyQuestions = {
    "Life":["Why is he so hairy","When will I die?","What is the meaning of life"]
    ,"Metaphysics":["Who invented God","When was the world created?","What created the elements?"]
    ,"Sex":["When can I have sex","Where did I come from?","What is a blow job?"]
}
n = random.randint(0,2)
n2 = random.randint(0,2)
RandomQ = list(babyQuestions.keys())[n]
RandomQ = babyQuestions[RandomQ][n2]
answer = input("{}?: ".format(RandomQ)).strip().lower()

while answer != "just because":
    n = random.randint(0,2)
    n2 = random.randint(0,2)
    RandomQ = list(babyQuestions.keys())[n]
    RandomQ = babyQuestions[RandomQ][n2]
    answer = input("{}?: ".format(RandomQ)).strip().lower()
    # continue
    # break
print("Oh...okay")