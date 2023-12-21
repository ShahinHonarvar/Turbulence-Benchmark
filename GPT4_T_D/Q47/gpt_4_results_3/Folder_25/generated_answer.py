
import re

def palindromes_of_specific_lengths(string):
    substring = string[26:85].lower()
    only_letters_substring = re.sub('[^a-z]', '', substring)
    palindromes = set()
    for i in range(len(only_letters_substring)):
        for j in range(i+30, min(i+47, len(only_letters_substring)+1)):
            if only_letters_substring[i:j] == only_letters_substring[i:j][::-1]:
                palindromes.add(only_letters_substring[i:j])
    return palindromes
