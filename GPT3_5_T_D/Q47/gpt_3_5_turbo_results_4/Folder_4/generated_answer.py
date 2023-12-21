
import string

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[12:93].lower()
    for length in range(17, 67):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i:i+length][::-1] and all(char in string.ascii_letters for char in substring[i:i+length]):
                palindromes.add(substring[i:i+length])
    return palindromes
