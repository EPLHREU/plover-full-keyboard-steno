from plover.system.english_stenotype import *

KEYS = ('e-', '`-', 't-', '1-', 'Q-', 'A-', 'Z-', '2-', 'W-', 'S-', 'X-', '3-', 'E-', 'D-', 'C-', '4-', 'R-', 'F-', 'V-', '5-', 'T-', 'G-', 'B-',
'_',
'-6', '-Y', '-H', '-N', '-7', '-U', '-J', '-M', '-8', '-I', '-K', '-,', '-9', '-O', '-L', '-.', '-0', '-P', '-;', '-s', '-d', '-[', '-q', '-=', '-]', '-b', '-\\', '-r')

IMPLICIT_HYPHEN_KEYS = ('_',)
SUFFIX_KEYS = ()
NUMBERS = {}
NUMBER_KEY = None
ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_WORDLIST = None
ORTHOGRAPHY_RULES_ALIASES = {}

KEYMAPS = {
    'Keyboard': {
        'e-' : 'Escape',
        '`-' : '`',
        't-' : 'Tab',
        '1-' : '1',
        'Q-' : 'q',
        'A-' : 'a',
        'Z-' : 'z',
        '2-' : '2',
        'W-' : 'w',
        'S-' : 's',
        'X-' : 'x',
        '3-' : '3',
        'E-' : 'e',
        'D-' : 'd',
        'C-' : 'c',
        '4-' : '4',
        'R-' : 'r',
        'F-' : 'f',
        'V-' : 'v',
        '5-' : '5',
        'T-' : 't',
        'G-' : 'g',
        'B-' : 'b',
        '_'  : 'space',
        '-6' : '6',
        '-Y' : 'y',
        '-H' : 'h',
        '-N' : 'n',
        '-7' : '7',
        '-U' : 'u',
        '-J' : 'j',
        '-M' : 'm',
        '-8' : '8',
        '-I' : 'i',
        '-K' : 'k',
        '-,' : ',',
        '-9' : '9',
        '-O' : 'o',
        '-L' : 'l',
        '-.' : '.',
        '-0' : '0',
        '-P' : 'p',
        '-;' : ';',
        '-s' : '/',
        '-d' : '-',
        '-[' : '[',
        '-q' : '\'',
        '-=' : '=',
        '-]' : ']',
        '-b' : 'BackSpace',
        '-\\' : '\\',
        '-r' : 'Return',
        'arpeggiate': 'F1',
    }
}
