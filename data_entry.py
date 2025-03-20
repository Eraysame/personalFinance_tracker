from datetime import datetime


def get_date(prompt, allow_defualt=False):
    date_str = input(prompt)
    if allow_defualt and not date_str:
        return datetime.today().strftime("%d-%m-%Y")

    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y")
        return valid_date.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. please enter date in dd-mm-yy format!")
        return get_date(prompt, allow_defualt)


def get_amount():
    pass


def get_category():
    pass


def get_description():
    pass
