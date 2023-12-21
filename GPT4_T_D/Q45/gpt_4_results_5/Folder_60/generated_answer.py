
from itertools import permutations

def palindromes_between_indices(my_string):
    my_string = my_string[3:7].lower()
    all_combinations = []
    result_set = set()
    for c in my_string:
        all_combinations += [''.join(p) for p in permutations(my_string)]
    for combo in all_combinations:
        if combo == combo[::-1] and len(combo) >= 4:
            result_set.add(combo)
    return result_set
