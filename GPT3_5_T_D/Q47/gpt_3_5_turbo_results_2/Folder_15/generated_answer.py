
import re

def palindromes_of_specific_lengths(string):
    substr = string[:7].lower()
    palindromes = set()
    
    for length in range(3, 7):
        for i in range(7 - length + 1):
            substring = substr[i:i+length]
            if re.match(r"^[a-zA-Z]+$", substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    
    return palindromes
