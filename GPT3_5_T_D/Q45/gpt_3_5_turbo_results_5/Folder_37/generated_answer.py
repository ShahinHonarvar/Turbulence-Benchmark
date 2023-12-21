
def palindromes_between_indices(string):
    import itertools
    import re
    
    # Extract the letters between index 1 and 4
    letters = re.findall('[a-zA-Z]', string[1:5])
    
    # Generate all possible arrangements of the letters
    arrangements = list(itertools.permutations(letters))
    
    palindromes = set()
    
    # Check each arrangement if it forms a palindrome of at least length 5
    for arrangement in arrangements:
        word = ''.join(arrangement).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
