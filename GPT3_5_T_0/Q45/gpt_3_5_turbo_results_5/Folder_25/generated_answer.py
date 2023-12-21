
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[a-zA-Z]', string)
    letters = [letter.lower() for letter in letters]
    
    palindromes = set()
    for length in range(3, 5):
        for combination in itertools.permutations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    
    return palindromes
