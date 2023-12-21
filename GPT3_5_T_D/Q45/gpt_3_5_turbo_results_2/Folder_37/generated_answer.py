
import itertools

def palindromes_between_indices(string):
    english_letters = ''.join(filter(str.isalpha, string.lower()))
    combinations = set(itertools.permutations(english_letters, 4))
    palindromes = set()

    for combo in combinations:
        palindrome = ''.join(combo) + ''.join(combo[::-1])
        if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)

    return palindromes
