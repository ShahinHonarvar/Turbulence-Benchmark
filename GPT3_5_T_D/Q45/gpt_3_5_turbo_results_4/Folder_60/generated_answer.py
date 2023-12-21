
import itertools

def palindromes_between_indices(string):
    letters = []
    for index in range(3,7):
        if string[index].isalpha():
            letters.append(string[index].lower())
    
    palindromes = set()
    for length in range(4, len(letters)+1):
        for combination in itertools.permutations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    
    return palindromes
