
import itertools

def palindromes_between_indices(string):
    # Get the English letters in the specified range
    letters = [c.lower() for c in string[1:6] if c.isalpha()]

    # Generate all possible arrangements of the English letters
    arrangements = list(itertools.permutations(letters))

    palindromes = set()
    # Check each arrangement for palindromes
    for arrangement in arrangements:
        word = ''.join(arrangement)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)

    return palindromes
