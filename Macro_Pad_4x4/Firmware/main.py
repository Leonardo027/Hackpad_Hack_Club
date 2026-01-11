print("Iniciando Hackpad do Hack Club!")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData

# --- CONFIGURAÇÃO BÁSICA ---
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# --- CONFIGURAÇÃO DA MATRIZ (PINOS) ---
# Linhas (Rows): P26(D0), P27(D1), P28(D2), P29(D3)
# Colunas (Cols): P6(D4), P7(D5), P0(D6), P4(D9)

keyboard.col_pins = (board.D4, board.D5, board.D6, board.D9)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- CONFIGURAÇÃO DO ENCODER ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Pinos do Encoder: A=P1(D7), B=P2(D8)
encoder_handler.pins = ((board.D7, board.D8, None, False),)

# O que o encoder faz ao girar? (Ex: Volume)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), # Gira esq, Gira dir, Botão (se fosse direto)
]

# --- CONFIGURAÇÃO DOS LEDS (RGB) ---
from kmk.extensions.RGB import RGB
rgb = RGB(pixel_pin=board.D10, num_pixels=16, val_limit=100, hue_default=100, sat_default=100, val_default=100)
keyboard.extensions.append(rgb)


# --- MAPA DE TECLAS (KEYMAP) ---

keyboard.keymap = [
    [
        # Linha 1 (Top)
        KC.N7,    KC.N8,    KC.N9,    KC.BSPC,
        # Linha 2
        KC.N4,    KC.N5,    KC.N6,    KC.PPLS,
        # Linha 3
        KC.N1,    KC.N2,    KC.N3,    KC.PMNS,
        # Linha 4 (Bottom)
        KC.N0,    KC.DOT,   KC.ENT,   KC.PAST,
    ]
]

if __name__ == '__main__':
    keyboard.go()