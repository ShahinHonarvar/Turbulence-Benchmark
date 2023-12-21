
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    for i in range(len(string)-90):
        for j in range(i+90, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                palindromes.add(string[i:j+1])
    
    return palindromes
