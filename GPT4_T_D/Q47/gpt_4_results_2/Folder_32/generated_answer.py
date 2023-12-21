
import re
def palindromes_of_specific_lengths(string):
    substr = string[16:78]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 43, min(i + 48, len(substr)+1)):
            test_str = substr[i:j]
            if (test_str == test_str[::-1]) and test_str.isalpha():
                palindromes.add(test_str.lower())
    return palindromes
