
from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[0:7]
    sub_string = sub_string.lower()
    all_possible_arrangements = [''.join(p) for p in permutations(sub_string)]
    
    palindromes = set()
    for arrangement in all_possible_arrangements:
        if len(arrangement) >= 3 and arrangement == arrangement[::-1]:
            palindromes.add(arrangement)
            
    return palindromes
