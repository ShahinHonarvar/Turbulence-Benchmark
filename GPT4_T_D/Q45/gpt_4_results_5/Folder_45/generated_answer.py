
from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    chars = [ch for ch in s if ch.isalpha()]
    all_combinations = set()
    for comb in permutations(chars):
        possible_palindrome = ''.join(comb)
        if possible_palindrome == possible_palindrome[::-1] and len(possible_palindrome) >= 4:
            all_combinations.add(possible_palindrome)
    return all_combinations
