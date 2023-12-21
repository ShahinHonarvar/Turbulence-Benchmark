
from itertools import permutations

def palindromes_between_indices(s):
    subset_string = s[6:10].lower()
    palindromes = set()
    for i in range(5, len(subset_string)+1):
        for j in permutations(subset_string, i):
            temp = ''.join(j)
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes
