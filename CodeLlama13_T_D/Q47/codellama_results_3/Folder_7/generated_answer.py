
def palindromes_of_specific_lengths(string):
    substr = string[119:257]
    return {palindrome for palindrome in substr.split() if len(palindrome) >= 104 and len(palindrome) <= 123 and all(c in 'abcdefghijklmnopqrstuvwxyz' for c in palindrome)}
