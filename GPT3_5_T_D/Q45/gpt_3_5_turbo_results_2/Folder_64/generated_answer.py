
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    from string import ascii_letters
    
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    
    english_letters = [c.lower() for c in string if c.isalpha()]
    english_counter = Counter(english_letters)
    range_letters = english_counter.most_common(10)[::-1]
    range_letters = [c * min(count, 2) for c, count in range_letters]
    
    possible_palindromes = set()
    for perm in itertools.permutations(range_letters, len(range_letters)):
        word = "".join(perm)
        if is_palindrome(word) and len(word) >= 5:
            possible_palindromes.add(word)
    
    return possible_palindromes
