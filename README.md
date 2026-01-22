# nikitabr0's hackpad
![IMG_20260103_002624](https://github.com/user-attachments/assets/0cffbcab-c0e3-4b67-bbb7-6a8ce52307a2)
[Demo video](https://youtu.be/7ATBC-yoFk0)

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/01eafb3b-19b2-4498-9282-4e710a8d48dc"</td>
    <td><img src="https://github.com/user-attachments/assets/c7764aa5-2316-48ad-9c05-62313e9f1dea"</td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/2421a1ec-f03d-427d-9370-2d949d4edbe4"</td>
    <td><img src="https://github.com/user-attachments/assets/421587ed-205d-4b86-bde2-0a2339d4e8cf"</td>
  </tr>
</table>   


My hackpad features 9 MX-style keyswitches and two EC11 rotary encoders. It has two modes: media control and gaming mode, the latter being mostly for simulators, that require large amounts of keybinds.

In media control mode the keys can be used for pausing, resuming and switching between audiotracks, as well as for using the calcuator (+, -, *, / and =), while the rotary encoders allow for audio volume and screen brightness control, with their switches set to muting audio and locking the screen.

In gaming mode all switches (including those of EC11s) register as F13-F22 presses, with the rotary encoders triggering Right CTRL + F13/14/15/16 on rotation. These keycodes were choosed as they are not included on most keyboards and thus largely unused.

The firmware if written in KMK for the sake of simplicity, although I may try rewriting it in QMK one day. The CAD was done in FreeCAD.

#

### Schematic
<img width="1203" height="816" alt="image" src="https://github.com/user-attachments/assets/f3137ff6-509e-4bd5-8dfc-eb0a1406cd08" />

### PCB layout
<img width="1026" height="736" alt="image" src="https://github.com/user-attachments/assets/e856f821-a921-4a49-8e11-43a76a06252b" />

### Case assembly
<img width="1236" height="870" alt="image" src="https://github.com/user-attachments/assets/a2bdf0f3-e2a3-487c-ad6c-dd724167b9b2" />
<img width="870" height="1016" alt="image" src="https://github.com/user-attachments/assets/4a9578e4-ffad-4b1e-a4a7-56be541e67b8" />

#

## Bill of materials:
- 1x Seeed XIAO RP2040 DIP
- 9x MX-style switches
- 2x EC11 rotary encoders
- 9x Blank DSA keycaps
- 11x Through-hole 1N4148 diodes
- 4x M3x5mx4mm heatset inserts

I will be printing the case by myself and as I already have some mounting hardware, I will be using it in this project:
- 4x M3x12 SHCS
- 3x M3x8 SHCS
