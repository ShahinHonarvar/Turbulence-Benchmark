
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = set()
    palindromes.update([string[i:i+27] for i in range(len(string)-26) if string[i:i+27] == string[i:i+27][::-1]])
    return palindromes
