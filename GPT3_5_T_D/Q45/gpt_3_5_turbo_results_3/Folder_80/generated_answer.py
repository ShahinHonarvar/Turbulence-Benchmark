
import itertools
import re

def palindromes_between_indices(string):
    english_letters = re.findall(r'[a-zA-Z]', string)

    if len(english_letters) < 6:
        return set()

    combinations = set(itertools.combinations(english_letters[3:9], 7))
    palindromes = set()

    for combination in combinations:
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome.lower())

    return palindromes
