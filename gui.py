from tkinter import *
from typing import Generator

root = Tk()


def next_value(values: Generator) -> int:
    return int(next(values))


def show_gui(type: str,
             title: str = None,
             ) -> None:
    """
    Shows GUI
    :param type: 'add' or 'a' to ADD new record, 'edit' or 'e' to EDIT existing record
    :param title: title of gui window
    :return: None
    """

    root.title(title)
    type = type.lower()
    label_col: int = 0
    entry_col: int = 1
    entry_width: int = 50
    rows: Generator[int, None, None] = (_ for _ in list(range(0, 15)))
    width: int = 2  # number of columns
    main_label_txt: str = ''
    notif_label_txt: str = ''
    url_label_txt: str = 'Address URL: '
    name_label_txt: str = 'Name: '
    log_label_txt: str = 'Login: '
    psw_label_txt: str = 'Password: '
    psw2_label_txt: str = 'Repeat password: '
    sec_label_txt: str = 'Security Level: '
    id_label_txt: str = 'ID number: '
    cre_label_txt: str = 'Creation date: '
    mod_label_txt: str = 'Last modification date: '
    try:
        assert type == 'add' or type == 'a' or type == 'edit' or type == 'e'
    except AssertionError as error:
        print(error)
        root.destroy()
        return
    else:
        if type == 'add' or type == 'a':
            main_label_txt: str = 'Fill the gaps to add a new record.'
        elif type == 'edit' or type == 'e':
            main_label_txt: str = 'Edit information about a record.'
            # TODO: fill input brackets with info from database

    # labels
    main_label: Label = Label(root, text=main_label_txt)
    notif_label: Label = Label(root, text=notif_label_txt)
    url_label: Label = Label(root, text=url_label_txt)
    name_label: Label = Label(root, text=name_label_txt)
    log_label: Label = Label(root, text=log_label_txt)
    psw_label: Label = Label(root, text=psw_label_txt)
    psw2_label: Label = Label(root, text=psw2_label_txt)
    sec_label: Label = Label(root, text=sec_label_txt)
    id_label: Label = Label(root, text=id_label_txt)
    cre_label: Label = Label(root, text=cre_label_txt)
    mod_label: Label = Label(root, text=mod_label_txt)

    # entries
    name_entry: Entry = Entry(root, width=entry_width)

    # grids
    main_label.grid(row=next_value(rows), columnspan=width, sticky=W+E)
    notif_label.grid(row=next_value(rows), columnspan=width, sticky=W+E)
    url_label.grid(row=next_value(rows), column=label_col, sticky=W)
    name_label.grid(row=next_value(rows), column=label_col, sticky=W)
    log_label.grid(row=next_value(rows), column=label_col, sticky=W)
    psw_label.grid(row=next_value(rows), column=label_col, sticky=W)
    psw2_label.grid(row=next_value(rows), column=label_col, sticky=W)
    sec_label.grid(row=next_value(rows), column=label_col, sticky=W)
    id_label.grid(row=next_value(rows), column=label_col, sticky=W)
    cre_label.grid(row=next_value(rows), column=label_col, sticky=W)
    mod_label.grid(row=next_value(rows), column=label_col, sticky=W)

    name_entry.grid(row=name_label.grid_info()['row'], column=entry_col, padx=10, sticky=E)


    # buttons

    print(name_label.grid_info())
    print(name_entry.grid_info())
    print(main_label.grid_info())


show_gui(type='a', title='Title')

root.mainloop()
