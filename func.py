import requests
import pandas as pd
from pathlib import Path
from typing import Any

import _constants as const
from utils.passprompt import PassPrompt
from utils.mysqlconn import MySQLConn


# def get_df_from_database() -> pd.DataFrame:
#     hostname: str = '127.0.0.1'
#     database: str = 'DB'
#     query_path: Path = Path('queries') / 'passes.sql'
#     pass_path: Path = Path('h.txt')
#     username, password = passprompt.PassPrompt(hashed=False).get_from_file(pass_path)
#     query = mysqlconn.query_from_path(query_path)
#     df = mysqlconn.MySQLConn(username, password, database, hostname).read_to_df(query)
#     return df

def create_conn() -> MySQLConn:
    """Creates connection instance with MySQL database"""
    log, psw = PassPrompt(hashed=False).get_from_file(const.__pass_path__)
    conn: MySQLConn = MySQLConn(log, psw,
                                const.__database__,
                                const.__hostname__)
    return conn


def check_notna(value: Any) -> bool:
    """Checks if value is not None"""
    if value is not None:
        return True
    else:
        return False


def check_url(url: str) -> bool:
    """Checks if url exists"""
    prefix = 'https://'
    if prefix not in url:
        url: str = prefix + url

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False
    else:
        if response.status_code == 200:
            return True
        else:
            return False


def check_match(values: list[str] | tuple[str]) -> bool:
    """Checks if values in list/tuple matches"""
    match: bool = False
    for i in range(1, len(values)):
        if values[i-1] == values[i]:
            match = True
        else:
            match = False

    return match


def check_exist(df: pd.DataFrame,
                query: str,
                conn: MySQLConn,
                cols: str | list[str] | tuple[str] | None = None
                ) -> bool:
    """Checks if record exists in database"""
    if cols is None:
        cols = ['URL', 'NAME', 'LOG']

    db: pd.DataFrame = conn.read_to_df(query, columns=cols)
    df: pd.DataFrame = df[cols]

    db['join'] = df[cols].agg(''.join, axis=1)
    df['join'] = df[cols].agg(''.join, axis=1)

    if db['join'].isin([df.loc[0, 'join']])[0]:
        return True
    else:
        return False
