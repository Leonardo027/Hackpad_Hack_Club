print("Iniciando Macropad...")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Configuração dos Pinos
# Colunas: P29, P6, P7
# Linhas: P26, P27, P28
keyboard.col_pins = (board.P29, board.P6, board.P7)
keyboard.row_pins = (board.P26, board.P27, board.P28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Configuração básica das 9 teclas (Camada 0)
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9,
    ]
]

if __name__ == '__main__':
    keyboard.go()