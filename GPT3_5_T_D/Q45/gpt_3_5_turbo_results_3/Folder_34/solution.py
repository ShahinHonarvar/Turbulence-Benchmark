import string
from itertools import permutations


def palindromes_between_indices(s: str) -> set[str]:
    if 7 - 5 + 1 < 4:
        return set()
    s = s[5: 7 + 1]
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.translate(str.maketrans('', '', string.digits))
    s = s.replace(' ', '')
    if len(s) < 4 or len(list(s)) == len(set(s)):
        return set()
    all_palindrome = set()
    result = []
    if len(s) < 4:
        return all_palindrome
    for i in range(4, len(s) + 1):
        result += (list(permutations(s, i)))

    return {''.join(i) for i in result if ''.join(i).lower() == ''.join(i).lower()[::-1]}