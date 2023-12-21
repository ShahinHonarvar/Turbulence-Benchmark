
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for n in range(70, len(string) + 1):
        for i in range(len(string) - n + 1):
            sub_string = string[i:i + n]
            if re.match(r'^[a-zA-Z]+$', sub_string):
                if sub_string == sub_string[::-1]:
                    palindromes.add(sub_string)
    return palindromes
