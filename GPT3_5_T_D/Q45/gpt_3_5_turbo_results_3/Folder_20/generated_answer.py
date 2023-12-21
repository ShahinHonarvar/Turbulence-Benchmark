
def palindromes_between_indices(string):
    import itertools
    import string as st
    
    letters = [letter.lower() for letter in string[2:9] if letter.lower() in st.ascii_letters]
    
    palindromes = set()
    
    for i in range(4, len(letters) + 1):
        for combination in itertools.permutations(letters, i):
            word = "".join(combination)
            if word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    
    return palindromes
