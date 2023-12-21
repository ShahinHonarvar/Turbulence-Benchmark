
def palindromes_between_indices(string):
    import itertools
    import string

    english_letters = string.ascii_letters
    arr = []

    for i in range(4):
        if string[i].lower() in english_letters:
            arr.append(string[i].lower())

    palindromes = set()

    for perm in itertools.permutations(arr):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)

    return palindromes
