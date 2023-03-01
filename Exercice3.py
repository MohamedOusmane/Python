def Occurence():
    chaine=input("Saisir une chaine de caractère:")
# Trier les caracteres de s pour éviter les répétitions
    caractere =set()

    for x in chaine:
        if x not in caractere:
            caractere.add(x)
        
            print("Le nombre d'occurrences du caractère: ", x, " dans la chaine est :", chaine.count(x))
    print(caractere)
    
    
####
def changerCasse(ch):
    chaineMod=""
    
    for e in ch:
        if e.isupper()==True:
            chaineMod=chaineMod+e.lower()
        else:
            chaineMod=chaineMod+e.upper()
    return chaineMod
    
###
def conjugaison(verbe):
    len(verbe)
    n=len(verbe)
    if verbe[n-2:n]!="er" or verbe=="aller":
        print("c'est un verbe de premier groupe")
    else:
        print("je",verbe[0:n-1])
        print("tu",verbe[0:n-1]+"s")
        print("il/elle",verbe[0:n-1])
        print("nous",verbe[0:n-2]+"ons")
        print("vous",verbe[0:n-2]+"ez")
        print("ils/elles",verbe[0:n-1]+"nt")
        
###
def Renverse(ch):
    chinv=""
    
    for i in range(len(ch)-1,-1,-1):
        chinv=chinv+ch[i]
    if chinv==ch:
        print("Palindrome",chinv)
    else:
        print("Non palindrome",chinv)
        
###
def occurence(ch,x):
   
    nbre=0
    for i in range(0,len(ch),1):
        if ch[i]==x:
            nbre=nbre+1
    return (nbre)
   
            
        
