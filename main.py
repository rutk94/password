import pyperclip as pc
import sys
from pathlib import Path
from subprocess import Popen, PIPE

github_token_file: Path = Path(r'/home/patryk/python/h.txt')

with open(github_token_file, 'rb') as file:
    token: bytes = file.readline()

if sys.platform == 'linux':
    p = Popen(args=['xsel', '-bi'], stdin=PIPE)
    p.communicate(input=token)
else:
    pc.copy(token)

print('token successfully copied to clipboard')
