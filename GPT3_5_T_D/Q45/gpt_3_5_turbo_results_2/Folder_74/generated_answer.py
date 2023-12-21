
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]

    palindromes = set()
    for comb in itertools.combinations(english_letters, 6):
        for perm in itertools.permutations(comb):
            palindrome = ''.join(perm)
            if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)

    return palindromes
