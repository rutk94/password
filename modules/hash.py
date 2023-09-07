import re
import string
import random
import pandas as pd
from pandas_ods_reader import read_ods
from pathlib import Path

random.seed(42)

file = Path('../unicode.ods')
df_raw = read_ods(file)
df = df_raw[['Decimal', 'Appearance']]
# file = Path('../unicode.xlsx')
# df_raw = pd.read_excel(file)
# df = df_raw[['Decimal', 'Appearance']]
# df['Decimal'] = df['Decimal'].astype('int64')


def coder(password: str) -> str:
    """
    Hides given text with coding algorithm.
    :param  password: text to code
    :return coded string
    """
    chars: list[str] = [char for char in password]

    decimals: list[int] = []
    for char in chars:
        decimal: int = df.where(df['Appearance'] == char).dropna().reset_index().loc[0, 'Decimal']
        decimals.append(decimal)

    randoms: list[str] = [random.choice(string.ascii_letters) for _ in range(len(decimals))]
    coders: list[str] = [str(decimals[i])+randoms[i] for i in range(len(decimals))]

    return "".join(coders)


def decoder(code: str) -> str:
    """
    Decode hidden text with algorithm.
    :param code: Hidden text
    :return: decoded string
    """
    letters: list[str] = re.findall(r'[a-zA-Z]', code)
    chars: list[str] = [char for char in code]
    slashed: list[str] = chars.copy()

    for letter in letters:
        slashed = list(map(lambda x: x.replace(letter, '/'), slashed))

    slashed_str: str = "".join(slashed[:-1])
    decimals: list[str] = slashed_str.split('/')
    decimals: list[int] = [int(decimal.replace('.0', '')) for decimal in decimals]

    letters: list[str] = []
    for decimal in decimals:
        letter: str = df.where(df['Decimal'] == decimal).dropna().reset_index().loc[0, 'Appearance']
        letters.append(letter)

    return "".join(letters)


print(coder('dcba'))
print(decoder('100.0O99.0h98.0b97.0V'))
