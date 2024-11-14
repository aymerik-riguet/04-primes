"""Importe la methode sqrt permettant de reduire le nombre de calcul dans la fonction secondaire"""


#### Fonction secondaire

def isprime(p):
    """Fonction qui permet de retourner la vérité de « p est un nombre premier »"""
    premier = True
    if p in (1,0) :
        return False
    for div in range (2,p) :
        if p % div == 0:
            premier = False
    return premier


#### Fonction principale

def main():
    """On ecrit quelques appels de la fonction secondaire afin de tester isprime"""
    # vos appels à la fonction secondaire ici
    print(isprime(8))
    print(isprime(11))
    print(isprime(15))
    print(isprime(17))
    for n in range(100):
        if isprime(n):
            print( n, end=", ")

    print()


if __name__ == "__main__":
    main()
