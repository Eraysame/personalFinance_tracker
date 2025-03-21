from datetime import datetime

date_format = "%d-%m-%Y"
categries = {"I": "Income", "E": "Expenses"}


def get_date(prompt, allow_defualt=False):
    date_str = input(prompt)
    if allow_defualt and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. please enter date in dd-mm-yy format!")
        return get_date(prompt, allow_defualt)


def get_amount():
    try:
        amount = float(input("please enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be non-negitive non-zero value")
        return amount

    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input(
        "enter the catogry ('I' for income or 'E' for expenses )").upper()
    if category in categries:
        return categries()

    print("invalid category, Please enter 'I' for Income or 'E' for Expenses.")
    return get_category()


def get_description():
    return input("Please enter a description 'optional': ")
