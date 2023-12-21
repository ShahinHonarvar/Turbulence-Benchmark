
def palindromes_between_indices(string):
    from itertools import permutations
    from re import findall
    result = set()
    letters = findall('[a-zA-Z]', string[2:8])
    if len(letters) < 6:
        return result
    for perm in permutations(letters, 6):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1]:
            result.add(palindrome)
    return result
