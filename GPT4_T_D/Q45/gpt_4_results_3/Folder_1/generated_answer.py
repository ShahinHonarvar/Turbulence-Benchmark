
from itertools import permutations

def palindromes_between_indices(string):
    string = string[4:8]
    lower_string = string.lower()
    arrangements = list(set(permutations(lower_string, 5)))
    palindromes = set()
    for arrangement in arrangements:
        combination = ''.join(arrangement)
        if combination == combination[::-1]:
            palindromes.add(combination)
    return palindromes
