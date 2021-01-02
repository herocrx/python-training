def one():
    print('Working hard')
    return "January"
 
def two():
    print('Working hard')
    return "February"
 
def three():
    print('Working hard')
    return "March"
 
def four():
    print('Working hard')
    return "April"
 
def five():
    print('Working hard')
    return "May"
 
def six():
    print('Vacation')
    return "June"
 
def seven():
    print('Vacation')
    return "July"
 
def eight():
    print('Vacation')
    return "August"
 
def nine():
    print('Working hard')
    return "September"
 
def ten():
    print('Working hard')
    return "October"
 
def eleven():
    print('Working hard')
    return "November"
 
def twelve():
    print('Working hard')
    return "December"
 
 
def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func