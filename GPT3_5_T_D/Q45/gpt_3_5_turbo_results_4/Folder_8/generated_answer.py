
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    string = string[1:6].lower()
    letters = [letter for letter in string if letter.isalpha()]
    freq = Counter(letters)
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = "".join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
