
import re

def palindrome_of_length_n(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Remove non-English letters
    string = re.sub('[^a-zA-Z]', '', string)
    
    palindromes = set()
    length = 91
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
