
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [char for char in s if char.isalpha()]
    palindrome_set = set()
    for i in range(4, len(letters)+1):
        possible_permutations = set(permutations(letters, i))
        for each in possible_permutations:
            string = ''.join(each)
            if string == string[::-1]:
                palindrome_set.add(string)
    return palindrome_set
