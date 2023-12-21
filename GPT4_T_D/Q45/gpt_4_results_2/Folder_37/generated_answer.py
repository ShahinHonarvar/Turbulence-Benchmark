
from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    combinations_of_word = []
    palindromes = set()
    
    for i in range(5, len(s)+1):
        combinations_of_word.extend([list(combinations(s, i)) for i in range(len(s), len(s)+1)])
        
    for combination in combinations_of_word:
        for word in combination:
            perms = [''.join(p) for p in permutations(word)]
            for perm in perms:
                if perm == perm[::-1]:
                    palindromes.add(perm)
                    
    return palindromes
