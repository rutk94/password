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
    pass


def check_ulr():
    pass


def check_match():
    pass


def check_exist():
    pass
