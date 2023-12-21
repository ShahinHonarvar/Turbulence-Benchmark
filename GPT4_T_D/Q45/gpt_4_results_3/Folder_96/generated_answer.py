
import itertools

def palindromes_between_indices(s):
    s = s[3:9]
    english_letters = "".join([char.lower() for char in s if char.isalpha()])
    permuts = list(itertools.permutations(english_letters))
    palindromes_set = set()

    for p in permuts:
        word = "".join(p)
        if len(word) >= 6 and word == word[::-1]:
            palindromes_set.add(word)

    return palindromes_set
