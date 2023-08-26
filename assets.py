from PIL import Image
from pathlib import Path

img_loc = Path(".assets/img/iffley_wall_big.png")
BASE_IMG = Image.open(img_loc)

COLOURS = {
    "normal": "blue",
    "stand": "green",
    "finish": "red",
}

HOLDS = {
    "left arete": (60, 730, 65, 1895),
    "right arete": (7006, 730, 7200, 1895),
    "left girder": (800, 5, 1010, 170),
    "middle girder": (3450, 5, 3650, 205),
    "right girder": (6125, 5, 6300, 205),
    1: (100, 1710, 350, 1890),
    2: (1200, 1710, 1340, 1890),
    3: (2000, 1675, 2150, 1790),
    4: (2350, 1710, 2550, 1890),
    5: (2880, 1710, 3010, 1830),
    6: (3380, 1710, 3525, 1830),
    7: (4270, 1710, 4405, 1830),
    8: (4655, 1710, 4790, 1830),
    9: (5125, 1710, 5365, 1830),
    10: (5745, 1710, 5865, 1830),
    11: (6675, 1710, 6820, 1830),
    12: (90, 1365, 250, 1540),
    13: (500, 1365, 650, 1540),
    14: (650, 1560, 920, 1700),
    "14A": (650, 1560, 815, 1700),
    "14B": (815, 1560, 920, 1700),
    15: (830, 1200, 1130, 1330),
    "15A": (830, 1200, 965, 1330),
    "15B": (965, 1200, 1050, 1330),
    "15C": (1050, 1200, 1130, 1330),
    16: (1200, 1365, 1450, 1540 - 50),
    17: (1650, 1540, 1790, 1670),
    18: (1570, 1200, 1830, 1330),
    19: (2335, 1365, 2470, 1480),
    20: (2645, 1365, 2790, 1480),
    21: (3010, 1410, 3150, 1670),
    22: (3015, 1200, 3150, 1330),
    23: (3465, 1365, 3600, 1480),
    24: (3765, 1540, 3910, 1670),
    25: (3695, 1200, 3830, 1330),
    26: (4150, 1365, 4290, 1480),
    27: (4395, 1540, 4530, 1670),
    28: (4380, 1200, 4520, 1330),
    29: (4765, 1365, 4900, 1480),
    30: (5170, 1365, 5310, 1480),
    31: (5495, 1540, 5630, 1670),
    32: (5490, 1200, 5630, 1330),
    33: (5610, 1365, 5750, 1480),
    34: (5990, 1540, 6130, 1670),
    35: (5990, 1200, 6130, 1330),
    36: (6365, 1540, 6500, 1670),
    37: (6490, 1080, 6630, 1330),
    38: (6740, 1200, 6880, 1330),
    39: (120, 850, 270, 1000),
    40: (390, 900, 530, 1150),
    "40A": (390, 900, 435, 1150),
    "40B": (435, 900, 530, 1150),
    41: (600, 560, 740, 810),
    "41A": (600, 560, 740, 765),
    "41B": (600, 765, 740, 810),
    42: (930, 690, 1060, 940),
    43: (1200, 850, 1310, 1000),
    44: (1560, 850, 1700, 1000),
    45: (1945, 1030, 2075, 1150),
    46: (1990, 850, 2380, 940),
    47: (2565, 1035, 2780, 1150),
    48: (2910, 850, 3150, 1000),
    49: (3270, 1035, 3400, 1150),
    50: (3515, 750, 3650, 1000),
    51: (4070, 1035, 4200, 1150),
    52: (3950, 850, 4075, 1000),
    53: (4495, 1035, 4620, 1150),
    54: (4740, 890, 4870, 1150),
    55: (5110, 1035, 5240, 1150),
    56: (5305, 850, 5440, 1000),
    57: (5730, 850, 5870, 1000),
    58: (6165, 1035, 6290, 1150),
    59: (6610, 850, 6750, 1000),
    60: (280, 380, 410, 640),
    61: (800, 350, 940, 490),
    "61A": (800, 350, 880, 490),
    "61B": (880, 350, 940, 490),
    62: (1180, 230, 1320, 490),
    "62A": (1180, 230, 1320, 410),
    "62B": (1180, 410, 1250, 490),
    63: (1300, 550, 1440, 670),
    64: (1680, 550, 1815, 670),
    "64A": (1680, 550, 1815, 580),
    "64B": (1750, 580, 1815, 670),
    65: (2045, 390, 2175, 505),
    66: (2410, 700, 2550, 830),
    67: (2520, 420, 2675, 670),
    68: (2790, 590, 2915, 830),
    69: (2910, 390, 3040, 505),
    70: (3020, 705, 3150, 830),
    71: (3140, 550, 3270, 670),
    72: (3150, 260, 3280, 505),
    "72A": (3150, 260, 3280, 460),
    "72B": (3150, 460, 3280, 505),
    73: (3380, 550, 3510, 670),
    74: (3510, 390, 3640, 505),
    75: (3870, 550, 4130, 670),
    76: (4120, 390, 4250, 505),
    77: (4250, 705, 4370, 830),
    78: (4250, 550, 4495, 670),
    79: (4555, 705, 4680, 830),
    80: (4735, 550, 4860, 670),
    81: (5125, 390, 5380, 505),
    82: (4980, 705, 5110, 830),
    83: (5370, 550, 5500, 670),
    84: (5610, 705, 5740, 830),
    85: (5865, 420, 6010, 670),
    86: (5975, 710, 6240, 830),
    "86A": (5975, 710, 6070, 780),
    "86B": (5975, 780, 6070, 830),
    "86C": (6070, 710, 6130, 830),
    "86D": (6130, 710, 6240, 780),
    "86E": (6130, 780, 6240, 830),
    87: (6230, 550, 6360, 670),
    88: (4730, 390, 4990, 505),
    89: (6480, 705, 6610, 830),
    90: (6610, 420, 6750, 670),
    91: (6780, 705, 6910, 830),
    92: (6870, 250, 7010, 500),
    93: (35, 175, 170, 330),
    94: (170, 0, 320, 140),
    95: (490, 175, 630, 330),
    96: (1450, 200, 1580, 330),
    "96A": (1450, 200, 1580, 270),
    "96B": (1450, 270, 1580, 325),
    97: (1450, 60, 1700, 190),
    98: (1755, 200, 1880, 330),
    99: (2050, 60, 2300, 190),
    100: (2390, 200, 2525, 355),
    101: (2660, 60, 2930, 190),
    102: (2780, 200, 2905, 355),
    103: (3030, 60, 3165, 190),
    104: (3330, 60, 3475, 190),
    105: (3760, 60, 3900, 190),
    106: (3865, 200, 4010, 355),
    107: (4120, 60, 4250, 190),
    108: (4310, 200, 4455, 355),
    109: (4610, 200, 4755, 355),
    110: (4860, 60, 4995, 190),
    111: (5130, 200, 5275, 355),
    112: (5380, 60, 5515, 190),
    113: (5500, 200, 5760, 355),
    114: (5885, 60, 6130, 190),
    115: (6115, 200, 6245, 355),
    116: (6360, 200, 6495, 355),
    117: (6545, 60, 6800, 190),
}
