import pyautogui
from pathlib import Path
from passlib.hash import pbkdf2_sha256


class PassPrompt:
    """
    Interactive prompt for username and password.
    """
    def __init__(self,
                 user_prompt: str = 'Type user name: \n',
                 pass_prompt: str = 'Type password: \n',
                 title_of_gui: str = 'Logging',
                 hashed: bool = True,
                 ) -> None:
        self.user_prompt: str = user_prompt
        self.pass_prompt: str = pass_prompt
        self.title_of_gui: str = title_of_gui
        self.hashed: bool = hashed

    def get_from_gui(self) -> tuple[str, str]:
        """
        Gets username and password from interactive GUI.
        If self.hashed == True (default), returned password will be hashed.
        :return: tuple(username, password)
        """
        username: str = ''
        password: str = ''
        try:
            while username == '':
                username = pyautogui.password(
                    text=self.user_prompt,
                    title=self.title_of_gui,
                    mask=''
                )
            while password == '':
                password = pyautogui.password(
                    text=self.pass_prompt,
                    title=self.title_of_gui,
                    mask='*'
                )
            assert username != ''
            assert password != ''
            if self.hashed:
                password = pbkdf2_sha256.hash(password)

            return username, password

        except AssertionError as error:
            print(error)

    def get_from_file(self,
                      pass_path: Path
                      ) -> tuple[str, str]:
        """
        Gets username and password from file.txt.
        File must contain two rows - 1st for username, 2nd for password.
        If self.hashed == True (default), returned password will be hashed.
        :param pass_path: path to file.txt
        :return: tuple(username, password)
        """
        try:
            assert pass_path.exists()
            with open(pass_path, 'r') as pass_file:
                username = pass_file.readline().strip()
                password = pass_file.readline().strip()
            assert username != ''
            assert password != ''
            if self.hashed:
                password = pbkdf2_sha256.hash(password)

            return username, password

        except AssertionError as error:
            print(error)
