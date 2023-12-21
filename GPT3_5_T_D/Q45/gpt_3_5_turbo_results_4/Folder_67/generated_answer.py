
import itertools

def palindromes_between_indices(string):
    # Extract the letters between index 2 and index 6
    letters = string[2:7]
    
    # Generate all possible arrangements of the letters
    arrangements = list(itertools.permutations(letters.upper()))
    
    # Filter out arrangements that are not palindromes
    palindromes = set()
    for arrangement in arrangements:
        word = ''.join(arrangement)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
