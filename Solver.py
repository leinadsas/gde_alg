import UI
import Grid

def count_paths(m, forbidden):
    dp = [[0 for _ in range(m)] for _ in range(m)]
    forbidden_set = set(forbidden)
    
    # Kezdőpont (bal alsó sarok) ellenőrzése
    if (m-1, 0) not in forbidden_set:
        dp[m-1][0] = 1  # Csak 1 út vezet a kezdőpontba (maga a kezdőpont)
    
    # Dinamikus programozás: jobbra és felfelé haladás
    for i in reversed(range(m)):       # Sorok alulról felfelé
        for j in range(m):             # Oszlopok balról jobbra
            if (i, j) == (m-1, 0):    # Kezdőpontot kihagyjuk (már beállítottuk)
                continue
            if (i, j) in forbidden_set:
                dp[i][j] = 0
            else:
                # Az aktuális mezőbe csak alulról (i+1, j) vagy balról (i, j-1) érkezhetünk
                from_down = dp[i+1][j] if i+1 < m else 0
                from_left = dp[i][j-1] if j-1 >= 0 else 0
                dp[i][j] = from_down + from_left
    
    return dp, dp[0][m-1]  # Visszaadjuk a DP táblát és a célmező értékét