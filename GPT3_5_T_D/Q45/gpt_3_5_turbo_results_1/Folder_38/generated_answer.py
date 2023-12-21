
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[3:9] if ch.isalpha()]
    palindromes = set()
    
    for length in range(5, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
