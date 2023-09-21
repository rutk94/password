from gui import GUI
# from . import hash

# create requirements.txt:

# create coder:
# create encoder:

# create database:

from pathlib import Path
from utils import mysqlconn, passprompt

# hostname: str = '127.0.0.1'
# database: str = 'DB'
# query_path: Path = Path('queries') / 'passes.sql'
# pass_path: Path = Path('h.txt')
# # username, password = passprompt.PassPrompt(hashed=False).get_from_gui()
# username, password = passprompt.PassPrompt(hashed=False).get_from_file(pass_path)
# query = mysqlconn.query_from_path(query_path)
# df = mysqlconn.MySQLConn(username, password, database, hostname).read_to_df(query)
#
# print(df.info())

GUI().add_record()

# TODO: save new password:
# request for input (tkinter)
# code the password
# connect to database
# save new record in database

# TODO: get password from database:
# connect to database
# load table
# load last value
# encode the password
# show results (password by '*')


