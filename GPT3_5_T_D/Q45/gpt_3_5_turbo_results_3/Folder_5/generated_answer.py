
def palindromes_between_indices(string):
    from itertools import permutations
    import string as eng_string

    eng_letters = set(eng_string.ascii_letters)
    letters_in_range = set(string[4:9]) & eng_letters

    if len(letters_in_range) == 0:
        return set()

    palindromes = set()
    for p in permutations(letters_in_range, 5):
        word = ''.join(p).lower()
        if word == word[::-1]:
            palindromes.add(word)

    return palindromes
