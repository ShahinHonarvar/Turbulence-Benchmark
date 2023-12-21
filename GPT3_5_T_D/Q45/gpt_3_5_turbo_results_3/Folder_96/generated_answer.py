
import itertools

def palindromes_between_indices(s):
    valid_chars = [c.lower() for c in s[3:9] if c.isalpha()]
    valid_chars_set = set(valid_chars)
    palindromes = set()
    for comb in itertools.permutations(valid_chars, len(valid_chars)):
        word = ''.join(comb)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes if len(palindromes) > 0 else set()
