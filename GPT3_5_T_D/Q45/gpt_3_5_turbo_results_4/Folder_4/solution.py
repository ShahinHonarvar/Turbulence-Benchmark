import string
from itertools import permutations


def palindromes_between_indices(s: str) -> set[str]:
    if 9 - 3 + 1 < 7:
        return set()
    s = s[3: 9 + 1]
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.translate(str.maketrans('', '', string.digits))
    s = s.replace(' ', '')
    if len(s) < 7 or len(list(s)) == len(set(s)):
        return set()
    all_palindrome = set()
    result = []
    if len(s) < 7:
        return all_palindrome
    for i in range(7, len(s) + 1):
        result += (list(permutations(s, i)))

    return {''.join(i) for i in result if ''.join(i).lower() == ''.join(i).lower()[::-1]}