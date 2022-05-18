# Exemple simple de récursivité avec la fonction puissance
def puissance_to(a, n):
    k = a
    p = 1
    if a > 0:
        if n > 0:
            while p < n:
                k *= a
                p += 1
            return k
        else:
            return 1
    else:
        return 0

c = input("Entrez un nombre entier positif : ")
d = input("Entrez une puissance (>= 0) : ")
calc = puissance_to(int(c), int(d))
print("" + str(c) + " puissance " + str(d) + " = " + str(calc))

