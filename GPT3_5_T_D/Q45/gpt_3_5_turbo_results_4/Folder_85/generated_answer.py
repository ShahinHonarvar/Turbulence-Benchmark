
import itertools

def palindromes_between_indices(string):
    letters = []
    for c in string[2:9]:
        if c.isalpha():
            letters.append(c.lower())
    combinations = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for combination in combinations:
        palindrome = ''.join(combination) + ''.join(combination[::-1])
        if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
