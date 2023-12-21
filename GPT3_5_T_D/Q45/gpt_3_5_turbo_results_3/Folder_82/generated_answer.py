
import itertools

def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter.lower() for letter in string if letter.isalpha()]
    combinations = list(itertools.combinations(letters, 6))
    for combo in combinations:
        palindrome = ''.join(combo) + ''.join(combo[::-1])
        if len(palindrome) >= 7 and palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    return palindromes
