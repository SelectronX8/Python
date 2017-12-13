# -*-coding:Latin-1 -*

import os

inventaire =[("pomme", 22), ("melons",4), ("poires", 18), ("fraises", 76), ("prunes", 51)]
inventaire_inverse=[(qtt,fruit) for fruit,qtt in inventaire]
inventaire_inverse.sort(reverse=True)
inventaire=[(fruit,qtt) for qtt,fruit in inventaire_inverse]
print ("liste triee ", inventaire)

os.system("pause")
