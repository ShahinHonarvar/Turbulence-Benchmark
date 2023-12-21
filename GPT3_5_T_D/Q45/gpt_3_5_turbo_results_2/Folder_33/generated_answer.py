
def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[7:10] if ch.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters, len(letters)):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
