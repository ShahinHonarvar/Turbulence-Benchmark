
import itertools

def palindromes_between_indices(string):
    english_letters = [x.lower() for x in string if x.isalpha()]
    combinations = set(itertools.combinations(english_letters, 8))
    palindromes = set()
    
    for combination in combinations:
        word = "".join(combination)
        if word == word[::-1]:
            palindromes.add(word)
            
    return palindromes
