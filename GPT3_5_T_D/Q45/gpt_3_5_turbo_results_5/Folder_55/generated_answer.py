
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    english_letters = [ch for ch in string if ch.isalpha()]
    possibilities = set(itertools.permutations(english_letters, 3))

    palindromes = set()
    for p in possibilities:
        if p[0] == p[2]:
            palindrome = ''.join(p).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
