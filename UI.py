import Config
import Grid
import Solver

# Felhasználóval való kommunikáció (input/output).
# Beolvassa a tábla méretét és a tiltott mezőket.
# Kiírja az eredményt.

def MainMenu():
    """
    Főmenü a program különböző funkcióinak eléréséhez.

    Lehetőségek:
    1. Labirintus méretének megadása.
    2. Labirintus megjelenítése.
    3. A kérdésre a válasz kiírása.
    4. A labirintus adatainak nullázása.
    0. Kilépés a programból.
    """
    while True:
        try:
            menu = int(input("""\nFőmenü:
                   1-es billentyű: Labirintus méretének megadása.
                   2-es billentyű: Labirintus megjelenítése.
                   3-as billentyű: A kérdésre a válasz kiírása.
                   4-es billentyű: A labirintus adatainak nullázása.
                   0-s billentyű: Kilépés

                   Melyik menüpontot választja? """))
            match menu:
                case 1:
                      # Labirintus méretének megadása.
                      while True:
                        try:
                            m = int(input("Adja meg a labirintus méretét (m ≥ 4): "))
                            if m >= 4:
                                print(f"A megadott méret: {m}")
                                break
                            else:
                                print("Hiba: A méret nem lehet kisebb 4-nél.")
                        except ValueError:
                            print("Hiba: Csak egész számot adjon meg.")
                case 2:
                      # Labirintus megjelenítése.
                case 3:
                      # A kérdésre a válasz kiírása.
                case 4:
                      # A labirintus adatainak nullázása.
                case 0:
                    print("Kilépés a programból.")
                    exit()
                case _:
                    print("Érvénytelen menüpont! Próbálja újra.")
        except ValueError:
            print("Hiba: Csak számokat adjon meg a menüpont kiválasztásához.")