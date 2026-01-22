import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]
keyboard.extensions.append(MediaKeys())


#   Define media control and game mode layers
TO_MEDIA = KC.DF(0)
TO_GAME = KC.DF(1)


encoder_handler.pins = ((board.D0, board.D1, None, True), (board.D2, board.D3, None, True),)

encoder_handler.map = [
    ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP), (KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP),), # Control volume and brightness

    ((KC.RCTRL(KC.F13), KC.RCTRL(KC.F14)), (KC.RCTRL(KC.F15), KC.RCTRL(KC.F16)),),    # Right control + F13/F14/F15/F16
]

keyboard.col_pins = (board.D6, board.D5, board.D4, board.D7,)
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.NO, KC.LGUI(KC.L), KC.AUDIO_MUTE, TO_GAME,                                  # Empty cell, mute, lock screen, switch to game mode
     KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK, KC.KP_EQUAL,    # Previous track, play/pause, next track, numpad equal
     KC.KP_PLUS, KC.KP_MINUS, KC.KP_ASTERISK, KC.KP_SLASH,],                        # Numpad keys: plus, minus, multiply, divide

    [KC.NO, KC.F13, KC.F14, TO_MEDIA,                                               # Empty cell, F13, F14, switch to media control
     KC.F15, KC.F16, KC.F17, KC.F18,                                                # F15, F16, F17, F18
     KC.F19, KC.F23, KC.F21, KC.F22,],                                              # F19, F20, F21, F22
                                                                                    # All function keys are for mapping in simulators
]


if __name__ == '__main__':
    keyboard.go()
