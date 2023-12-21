
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    indices_range = english_letters[6:9]
    palindromes = set()
    
    for i in range(4, len(indices_range)+1):
        for combination in itertools.combinations(indices_range, i):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    
    return palindromes
