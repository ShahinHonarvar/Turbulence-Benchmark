
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[4:10]
    all_palindromes = set()
    
    for i in range(5, len(sub_string)+1):
        for perm in permutations(sub_string, i):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                all_palindrome.add(candidate) 
                
    return all_palindromes
