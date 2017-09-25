#!/usr/bin/env python3

import os
from coder import Coder


_welcome = """
真•小鲜肉群 交流工具, v2.1
命令:   0 to encode
        q to quit
        any other key to decode
"""


def main():
    print(_welcome)

    while True:
        mode = input('\nCommand: ')

        if mode == 'q':
            return

        output = ''
        msg = input('Encode: ' if mode == '0' else 'Decode: ')
        if mode == '0':
            output = Coder.msg_to_code(msg)
            print(' "{}" 已复制'.format(output))
        else:
            output = Coder.code_to_msg(msg)
            print(' "{}" 已复制'.format(output))
        os.system('echo "{}" | pbcopy'.format(output))
        print('')


if __name__ == "__main__":
    main()
