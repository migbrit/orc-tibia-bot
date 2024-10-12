import pyautogui as pg

BATTLE_REGION = (1570, 424, 158, 59)
LOOT_REGION = (674, 344, 214, 216)

def battle_empty():
    return pg.locateOnScreen('imgs\\empty-battle.png', region=BATTLE_REGION)

def attacking_monster():
    return pg.locateOnScreen('imgs\\red-target-attacking.png', region=BATTLE_REGION, confidence=0.6) or pg.locateOnScreen('imgs\\red-target-defending.png', region=BATTLE_REGION, confidence=0.8)

def kill_monster():
    while True:
        if not battle_empty():
            print('pressing space because there are monsters in the game!') 
            pg.press('space')
            while attacking_monster(): 
                print('attacking monster, image location below VVV') 
                print(attacking_monster())
        else:
            get_loot()  

def get_loot():
    loot = pg.locateOnScreen('imgs\\dead-wasp.png', region=LOOT_REGION, confidence=0.7)
    print(loot)
    if loot != None:
        x, y = pg.center(loot)
        pg.moveTo(x, y)
        pg.click(button="right")
    
