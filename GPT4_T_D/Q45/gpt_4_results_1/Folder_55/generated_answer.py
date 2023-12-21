
import itertools
def palindromes_between_indices(s):
    s = s.lower()
    chars = s[0:3]
    combinations = set()
    for i in range(3, len(chars)+1):
        for comb in itertools.permutations(chars, i):
            possible_palindrome = "".join(comb)
            if possible_palindrome == possible_palindrome[::-1]:
                combinations.add(possible_palindrome)
    return combinations
