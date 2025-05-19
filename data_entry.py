from datetime import datetime
CATEGORIES={"I":"Income", "E":"Expense"}

def get_date(prompt,allow_default=False):
    date_str=input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    try:
        valid_date=datetime.strptime(date_str,"%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Please Enter a valid date format (dd-mm-yyyy)")
        return get_date(prompt,allow_default)

def get_amount():
    try: 
     amount= float(input("Enter the Amount: "))
     if amount<=0:
         raise ValueError("Amount must be non-negative and non-zero value")
     return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category=input("Enter the Category('I' for Income or 'E' for Expense)").upper()
    if category in CATEGORIES:
     return CATEGORIES[category]
    print("Invalid Category, Please Enter the correct and given Category")
    return get_category()


def get_description():
    return input("Enter a description. (optional)")

