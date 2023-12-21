
def palindromes_between_indices(string):
    import itertools
    string = string[2:9]
    english_letters = [c for c in string if c.isalpha()]
    english_letters = set(english_letters)
    palindromes = set()
    
    for length in range(4, len(english_letters) + 1):
        for combination in itertools.combinations(english_letters, length):
            for permutation in itertools.permutations(combination):
                word = ''.join(permutation)
                if word.lower() == word[::-1].lower():
                    palindromes.add(word)
    
    return palindromes
