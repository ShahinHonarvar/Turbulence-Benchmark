
def palindromes_between_indices(s):
    from itertools import permutations
    s = s[3:5]
    s = s.lower()
    letters = [ch for ch in s if ch.isalpha()]
    perms = [''.join(p) for p in permutations(letters) if len(p)>=3]
    return set(word for word in perms if word == word[::-1])
