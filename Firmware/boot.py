import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.D7,  # col
    source=board.D10, # row
    midi=False,
    mouse=False,
    storage=False,
    usb_id={'manufacturer': 'nikitabr0', 'product': 'Custom macropad'},
)
