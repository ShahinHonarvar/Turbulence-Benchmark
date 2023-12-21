
from itertools import permutations 

def palindromes_between_indices(s):
    substring = s[6:10]
    substring = substring.lower()

    all_possibilities = set()

    permutations_list = list(permutations(substring))

    for perm in permutations_list:
        arranged_string = ''.join(perm)
        if len(arranged_string)>=5 and arranged_string == arranged_string[::-1]:
            all_possibilities.add(arranged_string)
    return all_possibilities
