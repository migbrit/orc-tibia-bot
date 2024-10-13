import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import os
import json
import constants

def create_folder():
    if not os.path.exists(constants.FOLDER_NAME):
        os.mkdir(constants.FOLDER_NAME)

class Record:
    def __init__(self):
        create_folder()
        self.count = 0
        self.coordinates = []

    def photo(self):
        path = f'{constants.FOLDER_NAME}\\flag_{self.count}.png'
        x, y = pg.position()
        photo = pg.screenshot(region=(x - 3, y - 3, 7, 7))
        photo.save(path)
        self.count = self.count + 1
        coordinate_info = {
            'path': path,
            'down_hole': 0,
            'up_hole': 0,
            'wait': 10
        }
        self.coordinates.append(coordinate_info)
    
    def down_hole(self):
        last_coordinate = self.coordinates[-1]
        last_coordinate['down_hole'] = 1

    def up_hole(self):
        last_coordinate = self.coordinates[-1]
        last_coordinate['up_hole'] = 1

    def key_code(self, key):
        if key == keyboard.Key.esc:
            with open(f'{constants.FOLDER_NAME}/infos.json', 'w') as file:
                file.write(json.dumps(self.coordinates))
            return False
        if key == keyboard.Key.insert:
            self.photo()
        if key == keyboard.Key.page_down:
            self.down_hole()
        if key == keyboard.Key.page_up:
            self.up_hole()

    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()

record = Record()
record.start()