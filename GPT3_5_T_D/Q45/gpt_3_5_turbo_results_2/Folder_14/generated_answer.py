
import itertools

def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter for letter in string[4:6] if letter.isalpha()]
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    
    return palindromes
