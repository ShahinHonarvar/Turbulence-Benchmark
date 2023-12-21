
from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:9].lower()
    valid_chars = [char for char in sub_str if char.isalpha()]
    
    palindromes = set()
    for length in range(6, len(valid_chars) + 1):
        for perm in permutations(valid_chars, length):
            word = "".join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
