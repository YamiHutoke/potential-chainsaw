from datetime import datetime
def calculate(birthdate):
    today=datetime.today()
    age=today.year-birthdate.year
    if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
        age -= 1
    return age

def Cal():
    print("The Age Calculator")
    print("Please enter your birthdate(YYYY-MM-DD):")
    birthdate_str = input()

    
    
