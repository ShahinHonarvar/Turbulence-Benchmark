
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters

    letters = set(ascii_letters.lower())
    indices_range = range(1, 7)
    
    valid_letters = [letter.lower() for letter in string if letter.lower() in letters]
    if not valid_letters:
        return set()
    
    palindromes = set()
    
    for length in range(3, len(valid_letters) + 1):
        for permutation in permutations(valid_letters, length):
            if all(permutation[index] == permutation[length - 1 - index] for index in range(length // 2)):
                palindromes.add(''.join(permutation).lower())
    
    return palindromes
