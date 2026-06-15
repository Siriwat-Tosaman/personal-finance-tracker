import datetime
import file_handler

def date_time():
    return datetime.datetime.now()

question = input("Do you want to add a record or view records or search by category? (add/view/search) ")

try:
    if question == "view":
        file_handler.summary()

    elif question == "add":
        record_type = input("revenue or expense? ")
        if record_type == "revenue" or record_type == "expense":
            input_money = float(input("How much? "))
            Category = input("What category? ")
            Date = date_time().strftime("%Y-%m-%d %H:%M:%S")
            file_handler.add_record(record_type, input_money, Category, Date)
            print("your", record_type, "is", input_money)
            print("Calculating totals...")
            print("Record added successfully.")

            file_handler.summary_add()

    elif question == "search":
        search_category = input("Enter the category to search for: ")
        file_handler.summary_search(search_category)

    else:
        print("Please enter 'revenue' or 'expense' or 'search'.")
except ValueError:
    print("Please enter a valid number for the amount.")
except FileNotFoundError:
    print("The file 'records.txt' was not found. Please make sure it exists.")
except TypeError:
    print("An error occurred with the input types. Please check your inputs.")
except Exception as e:
    print(f"An error occurred: {e}")