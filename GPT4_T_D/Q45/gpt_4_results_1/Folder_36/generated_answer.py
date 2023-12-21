
from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[5:9].lower()
    letters = [c for c in sub_str if c.isalpha()]
    results = set()
    for l in range(3, len(letters)+1):
        for tuple_ in permutations(letters, l):
            possible_palindrome = ''.join(tuple_)
            if possible_palindrome == possible_palindrome[::-1]:
                results.add(possible_palindrome)
                
    return results
