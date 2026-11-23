def czy_bezpieczne(wiersz, kolumna, umieszczone):
    for w, k in enumerate(umieszczone):
        if k == kolumna or abs(k - kolumna) == abs(w - wiersz):
            return False
    return True

def generuj_rozwiazania(n=8, wiersz=0, umieszczone=[]):
    if wiersz == n:
        yield umieszczone
        return

    for kolumna in range(n):
        if czy_bezpieczne(wiersz, kolumna, umieszczone):
            yield from generuj_rozwiazania(n, wiersz + 1, umieszczone + [kolumna])

def rysuj_plansze(rozwiazanie):
    n = len(rozwiazanie)
    print("   " + " ".join(str(i) for i in range(n)))
    print("  +" + "--" * n + "-+----")
    for wiersz_idx, kolumna_idx in enumerate(rozwiazanie):
        wiersz_str = ["Q" if k == kolumna_idx else "." for k in range(n)]
        print(f"{wiersz_idx} | " + " ".join(wiersz_str) + " |")
    print("  +" + "--" * n + "-+----")

def main():
    
    
    # liczę wszystkie rozwiązania
    licznik = sum(1 for _ in generuj_rozwiazania(8))
    print(f"Liczba rozwiązań: {licznik}")

    # wypisuję pierwsze 3 rozwiązania
    print("\nPierwsze 3 rozwiązania:")
    gen = generuj_rozwiazania(8)
    for i in range(3):
        wynik = next(gen)
        print(f"\nRozwiązanie nr {i + 1}: {wynik}")
        rysuj_plansze(wynik)

if __name__ == "__main__":
    main()