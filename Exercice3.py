s = "Python est un langage de programmation"
# Trier les caracteres de s pour éviter les répétitions
caractere =set()

for x in s:
    if x not in caractere:
        caractere.add(x)
        
        print("Le nombre d'occurrences du caractère: ", x, " dans la chaine s est :", s.count(x))
print(caractere)
    