"""Constants."""

# pylint: disable=too-many-lines

MODS = {
    1: 'Wololo Kingdoms',
    2: 'Portuguese Civilization Mod III',
    3: 'Age of Chivalry',
    4: 'Sengoku',
    7: 'Realms',
    101: 'King of the Hippo'
}

SPEEDS = {
    100: 'slow',
    150: 'standard',
    169: 'standard', # de
    178: 'standard', # up15
    200: 'fast',
    237: 'fast' # up15
}

DE_MAP_NAMES = {
    9: 'Arabia',
    10: 'Archipelago',
    11: 'Baltic',
    12: 'Black Forest',
    13: 'Coastal',
    14: 'Continental',
    15: 'Crater Lake',
    16: 'Fortress',
    17: 'Gold Rush',
    18: 'Highland',
    19: 'Islands',
    20: 'Mediterranean',
    21: 'Migration',
    22: 'Rivers',
    23: 'Team Islands',
    24: 'Random',
    25: 'Scandinavia',
    26: 'Mongolia',
    27: 'Yucatan',
    28: 'Salt Marsh',
    29: 'Arena',
    30: 'King of the Hill',
    31: 'Oasis',
    32: 'Ghost Lake',
    33: 'Nomad',
    51: 'Mideast',
    # 59: Custom
    67: 'Acropolis',
    68: 'Budapest',
    69: 'Cenotes',
    70: 'City of Lakes',
    71: 'Golden Pit',
    72: 'Hideout',
    73: 'Hill Fort',
    74: 'Lombardia',
    75: 'Steppe',
    76: 'Valley',
    77: 'MegaRandom',
    78: 'Hamburger',
    79: 'CtR Random',
    80: 'CtR Monsoon',
    81: 'CtR Pyramid Descent',
    82: 'CtR Spiral',
    83: 'Kilimanjaro',
    84: 'Mountain Pass',
    86: 'Serengeti',
    87: 'Socotra',
    108: 'Indochina',
    112: 'Bog Islands',
    122: 'Alpine Lakes',
    125: 'Ravines',
    126: 'Wolf Hill',
    139: 'Golden Swamp',
    140: 'Four Lakes'
}

MAP_NAMES = {
    9: 'Arabia',
    10: 'Archipelago',
    11: 'Baltic',
    12: 'Black Forest',
    13: 'Coastal',
    14: 'Continental',
    15: 'Crater Lake',
    16: 'Fortress',
    17: 'Gold Rush',
    18: 'Highland',
    19: 'Islands',
    20: 'Mediterranean',
    21: 'Migration',
    22: 'Rivers',
    23: 'Team Islands',
    24: 'Random',
    25: 'Scandinavia',
    26: 'Mongolia',
    27: 'Yucatan',
    28: 'Salt Marsh',
    29: 'Arena',
    30: 'King of the Hill',
    31: 'Oasis',
    32: 'Ghost Lake',
    33: 'Nomad',
    34: 'Iberia',
    35: 'Britain',
    36: 'Mideast',
    37: 'Texas',
    38: 'Italy',
    39: 'Central America',
    40: 'France',
    41: 'Norse Lands',
    42: 'Sea of Japan (East Sea)',
    43: 'Byzantinum',
    48: 'Blind Random',
    49: 'Acropolis',
    50: 'Budapest',
    51: 'Cenotes',
    52: 'City of Lakes',
    53: 'Golden Pit',
    54: 'Hideout',
    55: 'Hill Fort',
    56: 'Lombardia',
    57: 'Steppe',
    58: 'Valley',
    59: 'MegaRandom',
    60: 'Hamburger',
    61: 'CtR Random',
    62: 'CtR Monsoon',
    63: 'CtR Pyramid Descent',
    64: 'CtR Spiral',
    66: 'Acropolis',
    67: 'Budapest',
    68: 'Cenotes',
    69: 'City of Lakes',
    70: 'Golden Pit',
    71: 'Hideout',
    72: 'Hill Fort',
    73: 'Lombardia',
    74: 'Steppe',
    75: 'Valley',
    76: 'MegaRandom',
    77: 'Hamburger',
    78: 'CtR Random',
    79: 'CtR Monsoon',
    80: 'CtR Pyramid Descent',
    81: 'CtR Spiral',
    82: 'Kilimanjaro',
    83: 'Mountain Pass',
    84: 'Nile Delta',
    85: 'Serengeti',
    86: 'Socotra',
    87: 'Amazon',
    88: 'China',
    89: 'Horn of Africa',
    90: 'India',
    91: 'Madagascar',
    92: 'West Africa',
    93: 'Bohemia',
    94: 'Earth',
    95: 'Canyons',
    96: 'Enemy Archipelago',
    97: 'Enemy Islands',
    98: 'Far Out',
    99: 'Front Line',
    100: 'Inner Circle',
    101: 'Motherland',
    102: 'Open Plains',
    103: 'Ring of Water',
    104: 'Snakepit',
    105: 'The Eye',
    125: 'Ravines'
}

MAP_SIZES = {
    120: 'tiny',
    144: 'small',
    168: 'medium',
    200: 'normal',
    220: 'large',
    240: 'giant',
    255: 'maximum'
}

COMPASS = {
    'northwest': [1/3.0, 0],
    'southeast': [1/3.0, 2/3.0],
    'southwest': [0, 1/3.0],
    'northeast': [2/3.0, 1/3.0],
    'center': [1/3.0, 1/3.0],
    'west': [0, 0],
    'north': [2/3.0, 0],
    'east': [2/3.0, 2/3.0],
    'south': [0, 2/3.0]
}

VALID_BUILDINGS = [
    10, 12, 14, 18, 19, 20, 31, 32, 42, 45, 47, 49, 50, 51, 63, 64, 68, 70, 71, 72,
    78, 79, 82, 84, 85, 86, 87, 88, 90, 91, 101, 103, 104, 105, 109, 116, 117, 129,
    130, 131, 132, 133, 137, 141, 142, 153, 155, 199, 209, 210, 234, 235, 236, 276,
    331, 357, 463, 464, 465, 484, 487, 488, 490, 491, 498, 562, 563, 564, 565, 584,
    585, 586, 587, 597, 598, 617, 621, 659, 661, 665, 667, 669, 673, 674, 734, 789,
    790, 792, 793, 794, 796, 797, 798, 800, 801, 802, 804, 1189
] + [1553, 387, 110, 785, 1002] + [1021, 1187, 1251] + [946, 947, 886, 888, 881, 879, 938, 871] # 5th Age, Realms, DE, Various
