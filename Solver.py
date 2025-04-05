import UI 
import Grid
from UI import m # UI modulból importáljuk az 'm' értéket
from Grid import forbidden # Grid modulból importáljuk a 'forbidden' értéket

# A dinamikus programozási algoritmus megvalósítása.
# Bemenet: tábla mérete és tiltott mezők.
# Kimenet: az elérési módok száma.

def count_paths(m, forbidden): #bemenet a labirintus mérete és tiltott mezők
    dp = [[0 for _ in range(m)] for _ in range(m)] #két dimenziós lista a labirintus méretével, kezdetben mindegyik 0
    forbidden_set = set(forbidden) # tiltott mezők halmaza az összes tiltott cellával a gyorsabb ellenőrzéshez
    
    if (m-1, 0) not in forbidden_set: #kezdőpont (bal alsó sarok) ne legyen tiltott
        dp[m-1][0] = 1 #kezdőpont beállítása
    
    for i in reversed(range(m)): #visszafelé iterálom a mátrix celláit i a sor
        for j in range(m): #j a oszlop
            if (i, j) in forbidden_set: # ha a mező tiltott 0 az érték
                dp[i][j] = 0
            else:                       # ha nem tiltott (és nem megyünk ki a mátrixból) összeadjuk az elérhető utak számát
                if i+1 < m:
                    dp[i][j] += dp[i+1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
    return dp, dp[0][m-1]           #visszatér a táblázattal (vizualizáció miatt később jól jöhet) és a jobb felső cella értékét, ami a lehetséges útvonalak számával egyenlő
