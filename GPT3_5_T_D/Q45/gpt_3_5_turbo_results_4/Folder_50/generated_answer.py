
import itertools

def palindromes_between_indices(string):
    sub_string = string[4:9]
    sub_string = [ch.lower() for ch in sub_string if ch.isalpha()]
    permutations = set(''.join(perm) for perm in itertools.permutations(sub_string))
    palindromes = set()
    for p in permutations:
        if p.lower() == p[::-1].lower() and len(p) >= 5:
            palindromes.add(p)
    return palindromes
