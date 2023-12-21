
from itertools import permutations

def palindromes_between_indices(s):
    unique_char = "".join(set(s[1:6].lower()))
    palindrome_set = set()
    for i in range(6, len(unique_char) + 1):
        for subset in permutations(unique_char, i):
            subset = "".join(subset)
            if subset == subset[::-1]:
                 palindrome_set.add(subset)
    return palindrome_set
