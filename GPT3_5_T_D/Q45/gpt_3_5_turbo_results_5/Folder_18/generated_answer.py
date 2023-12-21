
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for length in range(3, 7):
        arrangements = itertools.permutations(english_letters, length)
        
        for arrangement in arrangements:
            word = ''.join(arrangement)
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
