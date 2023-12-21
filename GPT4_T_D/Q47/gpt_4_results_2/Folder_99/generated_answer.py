
import re

def palindromes_of_specific_lengths(string):
    selected_substring = string[127:289]
    selected_substring = re.sub("[^a-zA-Z]", "", selected_substring.lower())
    palindromes = set()
    for i in range(len(selected_substring)):
        for j in range(i+119, min(i+142, len(selected_substring)+1)):
            substring = selected_substring[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
