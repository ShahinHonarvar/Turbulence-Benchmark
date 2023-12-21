
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [char for char in s if char.isalpha()]
    palindrome_set = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            string = ''.join(perm)
            if string == string[::-1]:
                palindrome_set.add(string)
    return palindrome_set
