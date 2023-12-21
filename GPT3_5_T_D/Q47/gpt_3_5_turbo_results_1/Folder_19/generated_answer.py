
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()[10:56]
    palindromes = set()
    for i in range(len(string)):
        for j in range(3, 8):
            if i + j <= len(string):
                substring = string[i:i+j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes
