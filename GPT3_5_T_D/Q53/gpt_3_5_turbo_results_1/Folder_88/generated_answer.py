
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub("[^a-zA-Z]", "", string).lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 27, len(string) + 1):
            sub = string[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
