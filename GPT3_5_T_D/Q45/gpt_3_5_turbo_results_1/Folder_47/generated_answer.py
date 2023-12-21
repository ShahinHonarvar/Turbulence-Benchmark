
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindrome_set = set()
    for permutation in itertools.permutations(english_letters, 5):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1]:
            palindrome_set.add(candidate)
    return palindrome_set
