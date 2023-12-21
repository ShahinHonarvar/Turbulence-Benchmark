
def palindromes_between_indices(string):
    import itertools

    english_letters = [ch for ch in string if ch.isalpha()]

    if len(english_letters) < 4:
        return set()

    possible_palindromes = set()
    for perm in itertools.permutations(english_letters, 4):
        palindrome = ''.join(perm).lower()
        if palindrome == palindrome[::-1]:
            possible_palindromes.add(palindrome)

    return possible_palindromes
