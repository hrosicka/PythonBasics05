import random

print("RANDOM EMOJI GENERATOR")
print("----------------------")

# random generator from emoji list
smileysList = ['\N{Watermelon}',
               '\N{Lemon}', 
               '\N{Coconut}', 
               '\N{Tomato}', 
               '\N{Grapes}', 
               '\N{Peach}', 
               '\N{Pear}', 
               '\N{Banana}']

for _ in range(5):
    smileys = random.choice(smileysList)
    print(smileys, end= " ")
