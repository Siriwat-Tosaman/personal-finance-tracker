def add_record(record_type, input_money, Category, Date):
    with open("records.txt", "a") as file:
        file.write(f"{record_type},{input_money}, {Category}, {Date}\n")

def view_records():
    with open("records.txt", "r") as file:
        records = file.read()
    return records

def summary():
    records = view_records()
    lines = records.split("\n")
    total_revenue = 0
    total_expense = 0
    for line in lines:
        if line.strip() != "":
            record_type = line.split(",")[0]
            input_money = line.split(",")[1]
            Category = line.split(",")[2]
            Date = line.split(",")[3]
            total_revenue += float(input_money) if record_type == "revenue" else 0
            total_expense += float(input_money) if record_type == "expense" else 0
            
            print(f"====== {record_type} ======\nAmount: {input_money} Bath\nCategory: {Category}\nDate: {Date}")
    total_balance = total_revenue - total_expense
    print(f"\nTotal Revenue: {total_revenue}")
    print(f"Total Expense: {total_expense}")
    print(f"========================================")
    print(f"======== Total Balance: {total_balance} =========")
    print(f"========================================")

def summary_search(search_category):
    records = view_records()
    lines = records.split("\n")
    total_revenue = 0
    total_expense = 0
    for line in lines:
        if line.strip() != "":
            record_type = line.split(",")[0]
            input_money = line.split(",")[1]
            Category = line.split(",")[2]
            Date = line.split(",")[3]
            if Category.strip() == search_category.strip():
                total_revenue += float(input_money) if record_type == "revenue" else 0
                total_expense += float(input_money) if record_type == "expense" else 0
                
                print(f"====== {record_type} ======\nAmount: {input_money} Bath\nCategory: {Category}\nDate: {Date}")
    total_balance = total_revenue - total_expense
    print(f"\nTotal Revenue for category '{search_category}': {total_revenue}")
    print(f"Total Expense for category '{search_category}': {total_expense}")
    print(f"========================================")
    print(f"======== Total Balance for category '{search_category}': {total_balance} =========")
    print(f"========================================")

def summary_add():
    records = view_records()
    lines = records.split("\n")
    total_revenue = 0
    total_expense = 0
    for line in lines:
        if line.strip() != "":
            record_type = line.split(",")[0]
            input_money = line.split(",")[1]
            Category = line.split(",")[2]
            Date = line.split(",")[3]
            total_revenue += float(input_money) if record_type == "revenue" else 0
            total_expense += float(input_money) if record_type == "expense" else 0
            
            #print(f"====== {record_type} ======\nAmount: {input_money} Bath\nCategory: {Category}\nDate: {Date}")
    total_balance = total_revenue - total_expense
    print(f"\nTotal Revenue: {total_revenue}")
    print(f"Total Expense: {total_expense}")
    print(f"========================================")
    print(f"======== Total Balance: {total_balance} =========")
    print(f"========================================")