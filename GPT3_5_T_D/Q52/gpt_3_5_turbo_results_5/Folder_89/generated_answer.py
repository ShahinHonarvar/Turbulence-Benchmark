
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)  # remove non-English letters
    string = string.lower()  # convert string to lowercase
    palindromes = set()
    
    for i in range(len(string) - 36):
        substring = string[i:i+37]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
