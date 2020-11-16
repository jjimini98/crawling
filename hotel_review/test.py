# just test


from afinn import Afinn
afinn = Afinn()

print(afinn.score("It's great but little uncomfortable"))
print(afinn.score("great"))
print(afinn.score("uncomfortable"))
