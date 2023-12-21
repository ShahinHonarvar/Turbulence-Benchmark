
import itertools

def palindromes_between_indices(d):
    s = d[2:7].lower()

    if len(s) < 3:
        return set()

    unique_s = set(s)
    palindromes = set()

    for word_len in range(3, len(s) + 1):
        for combination in itertools.permutations(unique_s, word_len):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    
    return palindromes
