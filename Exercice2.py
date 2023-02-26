#Conversion des secondes en Jours, heures , minutes et secondes
Secondes=int(input("Saisir le temps à convertir:"))
Jours = Secondes // (24 * 3600)
Secondes = Secondes % (24 * 3600)
Heures = Secondes // 3600
Secondes =Secondes% 3600   
Minutes = Secondes // 60
Secondes %= 60


print("Jours:",Jours,"Heures:",Heures,"Minutes:",Minutes,"Secondes:",Secondes)



