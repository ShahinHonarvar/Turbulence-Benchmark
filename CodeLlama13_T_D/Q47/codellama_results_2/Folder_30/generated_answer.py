
def palindromes_of_specific_lengths(string):
    return {palindrome for palindrome in string[14:90].split() if len(palindrome) in range(55, 72)}
