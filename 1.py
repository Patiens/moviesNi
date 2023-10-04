import random


def wyznacz_wyraz_aryt(pierwszy_wyraz, roznica, n):
    return pierwszy_wyraz * roznica ** (n - 1)


def wyznacz_wyraz_aryt_iteracyjnie(pierwszy_wyraz, roznica, n):
    wyraz = pierwszy_wyraz
    i = 1
    while i < n:
        wyraz += roznica
        i += 1
    return wyraz


def wyznacz_wyraz_aryt_rekrencyjnie(pierwszy_wyraz, roznica, n):
    if n == 1:
        return pierwszy_wyraz
    else:
        return roznica + wyznacz_wyraz_aryt_rekrencyjnie(pierwszy_wyraz, roznica, n-1)


def main():
    print("Podaj k (ile razy losowac dane wejsciowe)")
    k = int(input())
    for _ in range(k):
        pierwszy_wyraz = random.randrange(-100, 100)/10
        roznica = random.randrange(-100, 100)/10
        n = random.randrange(5, 200)

    print("pierwszy wyraz:", pierwszy_wyraz)
    print("roznica:", roznica)
    print("n:", 3)
    zwykly = wyznacz_wyraz_aryt(pierwszy_wyraz, roznica, n)
    iteracja = wyznacz_wyraz_aryt_iteracyjnie(pierwszy_wyraz, roznica, n)
    rekurencja = wyznacz_wyraz_aryt_rekrencyjnie(pierwszy_wyraz, roznica, n)
    print("n-ty wyraz:", zwykly)
    print("n-ty wyraz iteracyjnie:", iteracja)
    print("n-ty wyraz rekurencyjnie:", rekurencja)
    if(zwykly == iteracja and iteracja == rekurencja):
        print("wartosci takie same")
    else:
        print("wartosci sa rozne")

if __name__ == "__main__":
    main()
