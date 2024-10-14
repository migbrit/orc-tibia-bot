import pyautogui as pg
import constants

def battle_empty():
    return pg.locateOnScreen('imgs\\empty-battle.png', region=constants.BATTLE_REGION, confidence=0.8)

def attacking_monster():
    return pg.locateOnScreen('imgs\\red-target.png', region=constants.BATTLE_REGION, confidence=0.92) 
    # or pg.locateOnScreen('imgs\\red-black-target.png', region=constants.BATTLE_REGION, confidence=0.72)
  
def kill_monster(): 
    while battle_empty() == None:
        pg.press('space')
        print('monstro alvejado.')                           
        while attacking_monster() != None: 
            pg.sleep(1)
            print('esperando monstro morrer...')
        print('procurando outro monstro...')

def go_to_flag(path, wait):
    flag = pg.locateOnScreen(path, region=constants.MINI_MAP_REGION, confidence=0.8)
    print('going to... ', path)
    if flag:
        x, y = pg.center(flag)
        pg.moveTo(x, y)
        pg.click()
        pg.sleep(wait)

def check_player_position():
    return pg.locateOnScreen('imgs\\point-player.png', region=constants.MINI_MAP_REGION, confidence=0.8)

def get_loot():
    # loot = pg.locateOnScreen('imgs\\dead-wasp.png', region=constants.LOOT_REGION, confidence=0.7)
    # if loot:
    #     x, y = pg.center(loot)
    #     pg.moveTo(x, y)
    #     pg.click(button="right")
    pg.hotkey("alt","q")

def check_status(name, delay, position, rgb, button):
    print(f'checando {name}...')
    pg.sleep(delay)
    x, y = position
    if pg.pixelMatchesColor(x, y, rgb):
        pg.press(button)

def eat_food():
    print('comendo food...')
    pg.press('9')

def down_hole(should_down):
    if should_down:
        box = pg.locateOnScreen('imgs\\hole-down.png', region=constants.GAME_ACTION_REGION, confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(2)

def up_hole(should_up, anchor, plus_x, plux_y):
    if should_up:
        box = pg.locateOnScreen(anchor, region=constants.GAME_ACTION_REGION, confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x + plus_x, y + plux_y)
            pg.press('F12')
            pg.click()
