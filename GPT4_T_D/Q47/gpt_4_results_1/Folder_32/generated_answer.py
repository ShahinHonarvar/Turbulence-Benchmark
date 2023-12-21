
import re
def palindromes_of_specific_lengths(str):
    str = str[16:78]
    palindromes = set()
    for length in range(43, 48):
        for i in range(len(str) - length + 1):
            sub_string = str[i:i+length]
            if sub_string.lower() == sub_string[::-1].lower() and sub_string.replace(" ","").isalpha():
                palindromes.add(sub_string)
    return palindromes
