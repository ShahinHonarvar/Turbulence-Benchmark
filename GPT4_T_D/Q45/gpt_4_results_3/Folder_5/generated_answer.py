
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[4:9]
    sub_string = sub_string.lower()
    palindromes = set()
    for i in range(4, len(sub_string) + 1):
        for permut in permutations(sub_string, i):
            word = ''.join(permut)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
