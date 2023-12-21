
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    def is_palindrome(palindrome):
        return palindrome.lower() == palindrome.lower()[::-1]
    
    letters = [ch.lower() for ch in string[3:10]]
    letter_counts = Counter(letters)
    valid_letters = [letter for letter in letter_counts if letter.isalpha()]
    
    if not valid_letters:
        return set()
    
    palindromes = set()
    
    for perm in itertools.permutations(valid_letters):
        palindrome = ''.join(perm)
        if len(palindrome) >= 3 and is_palindrome(palindrome):
            palindromes.add(palindrome)
    
    return palindromes
