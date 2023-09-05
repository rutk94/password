import string
import random
from pandas_ods_reader import read_ods
from pathlib import Path

# load df
file = Path('../unicode.ods')
df_raw = read_ods(file)
df = df_raw[['Decimal', 'Appearance']]


def coder(password: str) -> str:
    """
    Hides given text with coding algorithm.
    :param  password: text to code
    :return coded string
    """
    letters: list[str] = [letter for letter in password]
    decimals: list[str] = df.where(df['Appearance'].isin(letters))['Decimal'].dropna().astype('int64').tolist()
    randoms: list[str] = [random.choice(string.ascii_letters) for _ in range(len(decimals))]
    coders: list[str] = [str(decimals[i])+randoms[i] for i in range(len(decimals))]
    return "".join(coders)


def decoder(code: str) -> str:
    """
    Decode hidden text with algorithm.
    :param code: Hidden text
    :return: decoded string
    """
    pass



print(coder('efgh'))
#
#
# print(df[['Decimal', 'Appearance']])
# print(df.info())
