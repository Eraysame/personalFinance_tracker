import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description


class CSV:
    CSV_FILE = "finance_date.csv"
    columns = ["date", "Amount", "Categroy", "description"]
    format = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(
                columns=cls.columns)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, Amount, Categroy, description):
        new_entry = {
            "date": date,
            "Amount": Amount,
            "Categroy": Categroy,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print("Entery added successfully")

    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.format)
        start_date = datetime.strptime(start_date, CSV.format)
        end_date = datetime.strptime(end_date, CSV.format)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filter_df = df.loc(mask)

        if filter_df.empty:
            print("There is no transaction found in the given date!")
        else:
            print(
                f"transaction from {start_date.strftime(CSV.format)} to {end_date.strftime(CSV.format)}")


def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of transaction or enter today's date: ",
                    allow_defualt=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


add()
