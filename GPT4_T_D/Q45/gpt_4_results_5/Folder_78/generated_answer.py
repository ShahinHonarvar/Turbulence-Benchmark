
from itertools import permutations

def palindromes_between_indices(s):
    chars_between_indices = s[6:9].lower()

    all_combinations = permutations(chars_between_indices)
    all_views = {''.join(combination) for combination in all_combinations}

    palindromes_set = set()

    for view in all_views:
        if len(view) >= 3 and view == view[::-1]:
            palindromes_set.add(view)

    return palindromes_set
