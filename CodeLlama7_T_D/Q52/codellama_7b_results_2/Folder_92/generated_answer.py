
import re

def palindrome_of_length_n(string):
    # Remove any non-letter characters from the string
    string = re.sub(r'\W', '', string)
    # Find all palindromes of length 10 in the string
    palindromes = []
    for i in range(len(string) - 9):
        substr = string[i:i+10]
        if substr == substr[::-1]:
            palindromes.append(substr)
    return set(palindromes)
