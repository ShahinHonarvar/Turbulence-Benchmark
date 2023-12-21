
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string if ch.isalpha()]
    start, end = 1, 6
    palindromes = set()
    
    for length in range(6, len(letters)+1):
        for chars in itertools.permutations(letters, length):
            if chars[:6] == chars[-1:-7:-1]:
                palindrome = ''.join(chars).lower()
                palindromes.add(palindrome)
    
    return palindromes
