
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[4:6] if ch.isalpha()]
    if not letters:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            palindrome = "".join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
