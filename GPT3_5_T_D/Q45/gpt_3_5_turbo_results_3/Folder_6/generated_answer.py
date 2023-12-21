
import itertools

def palindromes_between_indices(string):
    english_letters = [ch.lower() for ch in string if ch.isalpha()]
    all_palindromes = set()
    
    for length in range(4, 8):
        for combination in itertools.permutations(english_letters, length):
            palindrome = ''.join(combination)
            if palindrome.lower() == palindrome.lower()[::-1]:
                all_palindromes.add(palindrome)
    
    return all_palindromes
