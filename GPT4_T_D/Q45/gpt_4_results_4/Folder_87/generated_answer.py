
from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[3:10].lower()
    letters = [char for char in sub_string if char.isalpha()]
    palindrome_set = set()
    for i in range(3, len(letters)+1):
        perms = permutations(letters, i)
        for p in perms:
            p_string = ''.join(p)
            if p_string == p_string[::-1]:
                palindrome_set.add(p_string)
    return palindrome_set
