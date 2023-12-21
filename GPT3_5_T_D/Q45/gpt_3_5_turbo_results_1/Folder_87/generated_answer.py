
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    possible_arrangements = set(itertools.permutations(english_letters, 6))
    palindromes = set()
    
    for arrangement in possible_arrangements:
        word = ''.join(arrangement)
        if word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    
    return palindromes
