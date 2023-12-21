
def palindromes_between_indices(text):
    from itertools import permutations

    letters = [char.lower() for char in text[4:10] if char.isalpha()]
    palindromes = set()

    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
