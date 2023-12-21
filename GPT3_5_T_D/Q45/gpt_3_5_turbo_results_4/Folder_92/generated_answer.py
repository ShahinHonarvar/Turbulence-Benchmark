
def palindromes_between_indices(string):
    import itertools
    from collections import Counter

    letters = ''.join(filter(str.isalpha, string[4:8])).lower()
    permutations = set(''.join(permutation) for permutation in itertools.permutations(letters))
    palindromes = {permutation for permutation in permutations if Counter(permutation) == Counter(permutation[::-1])}

    return {palindrome for palindrome in palindromes if len(palindrome) >= 4}
