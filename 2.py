import random


def wyznacz_wyraz_geo(pierwszy_wyraz, iloraz, n):
    return pierwszy_wyraz * iloraz ** (n - 1)


def wyznacz_wyraz_geo_iteracyjnie(pierwszy_wyraz, iloraz, n):
    wyraz = pierwszy_wyraz
    i = 1
    while i < n:
        wyraz *= iloraz
        i += 1
    return wyraz


def wyznacz_wyraz_geo_rekrencyjnie(pierwszy_wyraz, iloraz, n):
    if n == 1:
        return pierwszy_wyraz
    else:
        return iloraz * wyznacz_wyraz_geo_rekrencyjnie(pierwszy_wyraz, iloraz, n - 1)


def main():
    print("Podaj k (ile razy losowac dane wejsciowe)")
    k = int(input())
    for _ in range(k):
        pierwszy_wyraz = random.randrange(0, 100)/10
        iloraz = random.randrange(0, 100)/10
        n = random.randrange(5, 200)

    print("pierwszy wyraz:", pierwszy_wyraz)
    print("iloraz:", iloraz)
    print("n:", n)
    zwykly = wyznacz_wyraz_geo(pierwszy_wyraz, iloraz, n)
    iteracja = wyznacz_wyraz_geo_iteracyjnie(pierwszy_wyraz, iloraz, n)
    rekurencja = wyznacz_wyraz_geo_rekrencyjnie(pierwszy_wyraz, iloraz, n)
    print("n-ty wyraz:", zwykly)
    print("n-ty wyraz iteracyjnie:", iteracja)
    print("n-ty wyraz rekurencyjnie:", rekurencja)
    if(zwykly == iteracja and iteracja == rekurencja):
        print("wartosci takie same")
    else:
        print("wartosci sa rozne")

if __name__ == "__main__":
    main()
