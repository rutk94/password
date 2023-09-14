import pandas as pd
import sqlalchemy as sql

from pathlib import Path


def query_from_path(query_path: Path) -> str:
    """
    Returns query from file.sql as a string
    :param query_path: path to file.sql
    :return: query string
    """
    try:
        assert query_path.exists()
        with open(query_path, 'r', encoding='utf-8') as query_file:
            query: str = query_file.read()
        assert query != ''
        return query
    except AssertionError as error:
        print(error)


class MySQLConn:
    """
    Represents connection to database on MySQL Server.
    """
    def __init__(self,
                 username: str,
                 password: str,
                 database: str,
                 hostname: str = '127.0.0.1',
                 ) -> None:
        self.username: str = username
        self.password: str = password
        self.database: str = database
        self.hostname: str = hostname

    def read_to_df(self,
                   query: str,
                   **kwargs
                   ) -> pd.DataFrame:
        """
        Create DataFrame from query result
        :param query: statement of sql query given to database
        :param kwargs: custom pandas.read_sql parameters
        :return: DataFrame object from database table
        """
        engine: sql.Engine = sql.create_engine(
            f"mysql+mysqlconnector://{self.username}:{self.password}@{self.hostname}/{self.database}"
        )
        with engine.connect() as conn:
            sql_query: sql.TextClause = sql.text(query)
            data: pd.DataFrame = pd.read_sql(sql_query, conn, **kwargs)
            return data
