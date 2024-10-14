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
        pg.sleep(1)
        actions.get_loot()
        actions.go_to_flag(coordinate['path'], coordinate['wait'])
        if actions.check_player_position:
            actions.kill_monster()
            pg.sleep(1)
            actions.get_loot()
            actions.go_to_flag(coordinate['path'], coordinate['wait'])
        actions.eat_food()
        actions.down_hole(coordinate['down_hole'])
        actions.up_hole(coordinate['up_hole'], f'{constants.FOLDER_NAME}\\anchor-floor-02.png', 420, 0)
        actions.up_hole(coordinate['up_hole'], f'{constants.FOLDER_NAME}\\anchor-floor-03.png', 147, 120)

             
# keyboard.wait('h')
# run()

while True:
    keyboard.wait('h')
    box = actions.attacking_monster()
    if box:
        print(f'Imagem encontrada na região: {box}')  # Exibe a coordenada e o tamanho da box encontrada
        # Converta os valores da box em inteiros simples
        box_int = (int(box.left), int(box.top), int(box.width), int(box.height))
        # Capturar a screenshot da região que a imagem foi encontrada
        screenshot = pg.screenshot(region=box_int)
        screenshot.save('captura_monstro.png')
        print('Screenshot salva como captura_monstro.png')
    else:
        print('Imagem não encontrada')



     