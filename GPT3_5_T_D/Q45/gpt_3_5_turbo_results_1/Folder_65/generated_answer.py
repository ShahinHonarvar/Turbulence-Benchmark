
def palindromes_between_indices(string):
    import itertools
    from collections import Counter

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    letters = []
    for c in string[:7]:
        if c.isalpha():
            letters.append(c.lower())

    count = Counter(letters)
    permutations = itertools.permutations(letters)

    palindromes = set()
    for perm in permutations:
        word = ''.join(perm)
        if is_palindrome(word) and len(word) >= 5:
            palindromes.add(word)

    return palindromes
