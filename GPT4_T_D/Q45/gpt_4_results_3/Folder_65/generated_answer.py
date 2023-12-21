
from itertools import permutations

def palindromes_between_indices(s):
    palindromes_set = set()
    s = s.lower()
    s_in_range = s[0:7]
    
    for i in range(5, len(s_in_range) + 1):
        for j in permutations(s_in_range, i):
            string = "".join(j)
            if string == string[::-1]:
                palindromes_set.add(string)
            
    return palindromes_set
