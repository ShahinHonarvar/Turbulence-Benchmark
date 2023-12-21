
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters

    english_letters = set(ascii_letters.lower())

    indices_range = string[:6].lower()
    indices_range = set(filter(lambda i: i in english_letters, indices_range))

    palindromes = set()

    for perm in permutations(indices_range, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word.lower())

    return palindromes
