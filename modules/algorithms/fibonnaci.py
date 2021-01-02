def calculate(number, memo = {}):
    if number in memo: 
        return memo[number]
    if number < 0: 
        return 0
    if number == 1:
        return 1
    memo[number] = calculate(number - 1, memo) + calculate(number - 2, memo)
    return memo[number]
