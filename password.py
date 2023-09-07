import re
import random
import string
import pandas as pd
from pathlib import Path
from pandas_ods_reader import read_ods


class GetPassword:
    """
    Copy password to clipboard from database after inputting url or name of webside
    """

    dict_filepath: Path = Path('./dict') / 'dict.ods'
    df_raw: pd.DataFrame = read_ods(dict_filepath, columns=[1, 2, 3, 4])

    def __init__(self) -> None:
        self.df: pd.DataFrame = self.df_raw.loc[:, [2, 4]]

    def code(self, text: str) -> str:
        """
        Hides given text with coding algorithm.
        :param  text: text to code
        :return coded string
        """
        chars: list[str] = [char for char in text]

        hashers: list[str] = []
        for char in chars:
            hasher: str = (self.df
                           .where(self.df.loc[:, 4] == char)
                           .dropna().astype('object').reset_index()
                           .loc[0, 2]
                           )
            hashers.append(hasher)

        randoms: list[str] = [random.choice(string.ascii_letters) for _ in range(len(hashers))]
        coders: list[str] = [str(hashers[i]) + randoms[i] for i in range(len(hashers))]

        return "".join(coders)

    def decode(self, text: str) -> str:
        """
        Decode hidden text with algorithm.
        :param text: Hidden text
        :return: decoded string
        """
        chars: list[str] = [char for char in text]
        letters: list[str] = re.findall(r'[a-zA-Z]', text)
        sep: str = random.choice(string.ascii_letters)

        for letter in letters:
            chars = list(map(lambda x: x.replace(letter, sep), chars))

        separated: str = "".join(chars[:-1])
        hashers: list[str] = separated.split(sep)
        hashers: list[int] = [int(hasher.replace('.0', '')) for hasher in hashers]

        unhashed: list[str] = []
        for hasher in hashers:
            unhasher: str = (self.df
                             .where(self.df.loc[:, 2] == hasher)
                             .dropna().reset_index()
                             .loc[0, 4]
                             )
            unhashed.append(str(unhasher))

        return "".join(unhashed)
