from datetime import datetime
from tkinter import *
from typing import Generator


def next_value(values: Generator) -> int:
    return int(next(values))


class GUI:
    """
    Represents GUI
    """
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Password')
        self.label_col: int = 0
        self.entry_col: int = 1
        self.entry_width: int = 50
        self.rows: Generator[int, None, None] = (_ for _ in list(range(0, 15)))
        self.width: int = 2  # number of columns

        self.main_label_txt: str = ''
        self.url_label_txt: str = 'Address URL: '
        self.name_label_txt: str = 'Name: '
        self.log_label_txt: str = 'Login: '
        self.psw_label_txt: str = 'Password: '
        self.psw2_label_txt: str = 'Repeat password: '
        self.sec_label_txt: str = 'Security Level: '
        self.id_label_txt: str = 'ID number: '
        self.cre_label_txt: str = 'Creation date: '
        self.mod_label_txt: str = 'Last modification date: '

        self.notif_label_txt: StringVar = StringVar()
        self.sec_val: StringVar = StringVar()
        self.id_val: StringVar = StringVar()
        self.cre_val: StringVar = StringVar()

        # labels
        self.main_label: Label = Label(self.root, text=self.main_label_txt)
        self.url_label: Label = Label(self.root, text=self.url_label_txt)
        self.name_label: Label = Label(self.root, text=self.name_label_txt)
        self.log_label: Label = Label(self.root, text=self.log_label_txt)
        self.psw_label: Label = Label(self.root, text=self.psw_label_txt)
        self.psw2_label: Label = Label(self.root, text=self.psw2_label_txt)
        self.sec_label: Label = Label(self.root, text=self.sec_label_txt)
        self.id_label: Label = Label(self.root, text=self.id_label_txt)
        self.cre_label: Label = Label(self.root, text=self.cre_label_txt)
        self.mod_label: Label = Label(self.root, text=self.mod_label_txt)

        self.notif_label: Label = Label(self.root, textvariable=self.notif_label_txt)
        self.sec_val_label: Label = Label(self.root, textvariable=self.sec_val)
        self.id_val_label: Label = Label(self.root, textvariable=self.id_val)
        self.cre_val_label: Label = Label(self.root, textvariable=self.cre_val)

        # entries
        self.url_entry: Entry = Entry(self.root, width=self.entry_width)
        self.name_entry: Entry = Entry(self.root, width=self.entry_width)
        self.log_entry: Entry = Entry(self.root, width=self.entry_width)
        self.psw_entry: Entry = Entry(self.root, show='*', width=self.entry_width)
        self.psw2_entry: Entry = Entry(self.root, show='*', width=self.entry_width)

        # buttons
        self.save_button: Button = Button(self.root, text='SAVE', command=self.save)
        self.back_button: Button = Button(self.root, text='BACK', command=self.back)
        self.clear_button: Button = Button(self.root, text='CLEAR', command=self.clear)
        
    def save(self) -> None:
        """
        Saves information from frame to MySQL table.
        :return: None
        """
        # check password matching
        if self.psw_entry.get() != self.psw2_entry.get():
            self.notif_label_txt.set("Password doesn't match! Try again")
            self.psw_entry.configure(fg='red')
            self.psw2_entry.configure(fg='red')
            return
        else:
            self.notif_label_txt.set("Saving record to database.")
            self.psw_entry.configure(fg='green')
            self.psw2_entry.configure(fg='green')
            # TODO: pop-up with success info

        # connect to database
        # check if record exists
        pass

    def back(self) -> None:
        """
        Undoes the last change in frame.
        :return: None
        """
        pass

    def clear(self) -> None:
        """
        Clears out all the changes in frame.
        :return: None
        """
        self.url_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.log_entry.delete(0, END)
        self.psw_entry.delete(0, END)
        self.psw2_entry.delete(0, END)

    def add_record(self) -> None:
        """
        Shows frame for adding a new record.
        :return: None
        """
        self.main_label_txt: str = 'Fill the gaps to add a new record.'

        # labels grids
        self.main_label.grid(row=next_value(self.rows), columnspan=self.width, sticky=W + E)
        self.notif_label.grid(row=next_value(self.rows), columnspan=self.width, sticky=W + E)
        self.url_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.name_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.log_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.psw_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.psw2_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.sec_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.id_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.cre_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        # mod_label.grid(row=next_value(self.rows), column=self.label_col, sticky=W)
        self.sec_val_label.grid(row=self.sec_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=W)
        self.id_val_label.grid(row=self.id_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=W)
        self.cre_val_label.grid(row=self.cre_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=W)

        # entries grids
        self.url_entry.grid(row=self.url_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=E)
        self.name_entry.grid(row=self.name_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=E)
        self.log_entry.grid(row=self.log_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=E)
        self.psw_entry.grid(row=self.psw_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=E)
        self.psw2_entry.grid(row=self.psw2_label.grid_info()['row'], column=self.entry_col, padx=10, sticky=E)

        # buttons grids
        self.back_button.grid(row=next_value(self.rows), column=self.label_col, sticky=W + E)
        self.clear_button.grid(row=self.back_button.grid_info()['row'], column=self.entry_col, sticky=W + E)
        self.save_button.grid(row=next_value(self.rows), columnspan=self.width, sticky=W + E)

        self.root.mainloop()

    def edit_record(self) -> None:
        """
        Shows frame for editing an existing record.
        :return: None
        """
        pass
