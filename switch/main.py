
from usage import months

def main():
    # input a month from a keyboard
    month = input('Select month: ')
    # import a function from other module
    action = months.numbers_to_months(int(month))
    # execute action
    action()
    

if __name__ == "__main__":
    main()