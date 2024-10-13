import pyautogui as pg
import actions
import keyboard
import constants
import json

#Abrir OBS                    
#Deixar OBS em modo janela grande
#Rodar window.py para diminuir opacidade do Tibia
#Rodar o main.py

pg.useImageNotFoundException(False)

def run():
    with open(f'{constants.FOLDER_NAME}\\infos.json', 'r') as file:
        coordinates = json.loads(file.read())
    for coordinate in coordinates:
        actions.kill_monster()
        actions.get_loot()
        actions.go_to_flag(coordinate['path'], coordinate['wait'])
        if actions.check_player_position:
            actions.kill_monster()
            actions.get_loot()
            actions.go_to_flag(coordinate['path'], coordinate['wait'])
        actions.eat_food()
        actions.down_hole(coordinate['down_hole'])
        actions.up_hole(coordinate['up_hole'], f'{constants.FOLDER_NAME}\\anchor-floor-02.png', 420, 0)
        actions.up_hole(coordinate['up_hole'], f'{constants.FOLDER_NAME}\\anchor-floor-03.png', 147, 120)

run()



     