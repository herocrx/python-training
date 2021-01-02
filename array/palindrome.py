def isPalindrome(word):
    for index in range(0, int(len(word) / 2)):
        if word[index] != word[len(word) - 1 - index]: 
            return False
    return True
        

print(isPalindrome('Hubert'))
print(isPalindrome('Banana'))
print(isPalindrome('kajak'))