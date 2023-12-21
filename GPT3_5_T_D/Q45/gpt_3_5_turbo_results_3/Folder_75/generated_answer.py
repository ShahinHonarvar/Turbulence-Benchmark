
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[2:5] if ch.isalpha()]
    palindromes = set()
    for arrangement in itertools.permutations(letters):
        palindrome = ''.join(arrangement)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome.lower())
    return palindromes
