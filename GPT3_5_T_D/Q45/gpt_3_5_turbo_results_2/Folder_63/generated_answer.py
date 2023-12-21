
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:4] if c.isalpha()]
    if len(letters) < 3:
        return set()
    else:
        all_palindromes = set()
        for permutation in itertools.permutations(letters):
            palindrome = ''.join(permutation)
            if palindrome == palindrome[::-1]:
                all_palindromes.add(palindrome)
        return all_palindromes
