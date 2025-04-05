import UI
import Config

# A fő belépési pont a programhoz.
# Meghívja a felhasználói felületet (UI-t), kezeli a futás logikáját.

Config.clear_terminal()

quit = 1
while quit != 0:
    quit = UI.MainMenu()