print("="*3,"Calculatrice ","="*3)
print("\n" *2)
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
print("\n")
choix = input("Choix :")
premierNombre = input("entrer le premier nombre")
deuxiemeNombre = input("entrer le deuxieme nombre")

if choix == 1 or choix == "Addition" :
    resultat = premierNombre + deuxiemeNombre
elif choix == 2 or choix == "Soustraction":
    resultat = premierNombre - deuxiemeNombre
elif choix == 3 or choix == "Multiplication":
    resultat = premierNombre * deuxiemeNombre
else :
    resultat = premierNombre / deuxiemeNombre if deuxiemeNombre != 0 else resultat = "Pas de division par Zero"

print(resultat)