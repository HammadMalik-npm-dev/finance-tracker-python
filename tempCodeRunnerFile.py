import pandas as pd
import csv 
from datetime import datetime
from data_entry import get_amount,get_category,get_date,get_description

class CSV:
    CSV_FILE="finance_data.csv"
    COLUMNS=["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    @classmethod 
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("Entry added successfully")

CSV.initialize_csv()
CSV.add_entry("20-09-2025",3500,"Income","Salary")

def add():
    CSV.initialize_csv()
    date=get_date("Enter the Date (dd-mm-yyyy) or Press Enter for today's date"
                  ,allow_default=True)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)
add()