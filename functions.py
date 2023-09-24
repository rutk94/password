import pandas as pd
from pathlib import Path

from utils import passprompt, mysqlconn


def get_df_from_database() -> pd.DataFrame:
    hostname: str = '127.0.0.1'
    database: str = 'DB'
    query_path: Path = Path('queries') / 'passes.sql'
    pass_path: Path = Path('h.txt')
    username, password = passprompt.PassPrompt(hashed=False).get_from_file(pass_path)
    query = mysqlconn.query_from_path(query_path)
    df = mysqlconn.MySQLConn(username, password, database, hostname).read_to_df(query)
    return df
