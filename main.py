import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_date.csv"
    columns = ["Date", "Amount", "Categroy", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(
                columns=cls.columns)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, Date, amount, Categroy, description):
        new_entry = {
            "Date": Date,
            "amount": amount,
            "Categroy": Categroy,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)


CSV.initialize_csv()
