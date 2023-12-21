
import itertools
import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string)
    letters = [letter.lower() for letter in letters]
    letters = letters[3:10]
    combinations = list(itertools.permutations(letters))
    palindromes = set()
    for combination in combinations:
        if combination == combination[::-1]:
            palindrome = ''.join(combination)
            palindromes.add(palindrome)
    return palindromes
