from string import punctuation


_separator = u'\u2063'
_plus = u'\u2064'
let_to_code = { 'a': '._', 'b': '_...', 'c': '_._.',
                'd': '_..', 'e': _plus + '.', 'f': '.._.',
                'g': '__.', 'h': _plus + '....', 'i': _plus + '..',
                'j': '.___', 'k': '_._', 'l': '._..',
                'm': '__', 'n': '_.', 'o': '___',
                'p': '.__.', 'q': '__._', 'r': '._.',
                's': _plus + '...', 't': _plus + '_', 'u': '.._',
                'v': '..._', 'w': '.__', 'x': '_.._',
                'y': '_.__', 'z': '__..',

                'A': _plus + '._', 'B': _plus + '_...', 'C': _plus + '_._.',
                'D': _plus + '_..', 'E': _plus + _plus + '.', 'F': _plus + '.._.',
                'G': _plus + '__.', 'H': _plus + _plus + '....', 'I': _plus + _plus + '..',
                'J': _plus + '.___', 'K': _plus + '_._', 'L': _plus + '._..',
                'M': _plus + '__', 'N': _plus + '_.', 'O': _plus + '___',
                'P': _plus + '.__.', 'Q': _plus + '__._', 'R': _plus + '._.',
                'S': _plus + _plus + '...', 'T': _plus + _plus + '_', 'U': _plus + '.._',
                'V': _plus + '..._', 'W': _plus + '.__', 'X': _plus + '_.._',
                'Y': _plus + '_.__', 'Z': _plus + '__..',

                '0': '_____', '1': '.____', '2': '..___',
                '3': '...__', '4': '...._', '5': _plus + '.....',
                '6': '_....', '7': '__...', '8': '___..',
                '9': '____.',
}

simple_encode = lambda char: let_to_code.get(char, char)
simple_decode = lambda value: next(key for key in let_to_code if let_to_code[key] == value)


class Coder(object):
    @staticmethod
    def msg_to_code(msg):
        code = list()
        for char in msg:
            # alphanumeric
            if char in let_to_code:
                code.append(simple_encode(char))
            # punctuations
            elif char in punctuation:
                code.append(char)
            # unicode-only
            else:
                code.append(Coder._char_to_code(char))
        return ' '.join(code)

    @staticmethod
    def code_to_msg(code_str):
        msg = list()
        for code in code_str.split(' '):
            # space
            if code == '':
                msg.append(' ')
            # alphanumeric and punctuations
            elif len(code) < 8:
                msg.append(code if len(code) == 1 else simple_decode(code))
            # unicode
            else:
                msg.append(Coder._code_to_char(code))
        return ''.join(msg)

    @staticmethod
    def _char_to_code(char: str) -> str:
        raw = str(char.encode('unicode-escape'))
        code = list()
        for c in raw[4:-1]:
            code.append(simple_encode(c))
        return _separator.join(code)

    @staticmethod
    def _code_to_char(code: str) -> str:
        chars = ['\\']
        for char in code.split(_separator):
            chars.append(simple_decode(char))
        return bytes(''.join(chars), 'utf-8').decode('unicode-escape')
