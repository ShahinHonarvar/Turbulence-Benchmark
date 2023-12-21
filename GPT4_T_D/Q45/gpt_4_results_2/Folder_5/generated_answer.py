
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[4:9].lower()
    letters = [ch for ch in substr if ch.isalpha()]
    result = set()
    for i in range(4, len(letters)+1):
        for perm in permutations(letters, i):
            temp = ''.join(perm)
            if temp == temp[::-1]:
                result.add(temp)
    return result
