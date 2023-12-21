
from itertools import permutations

def palindromes_between_indices(string):
    # extract substring from the 2nd index to the 9th index
    substr = string[2:10]
    substr = substr.lower() # convert to lower case
    # initialize set
    palindromes_set = set()
    # generate all possible permutations
    for i in range(4, len(substr) + 1):
        perms = permutations(substr, i)
        for perm in perms:
            # create word from permutation and check if it is a palindrome
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes_set.add(word)
    return palindromes_set
