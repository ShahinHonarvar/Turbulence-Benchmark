
def palindromes_between_indices(string):
    import itertools

    letters = []
    for char in string[3:6]:
        if char.isalpha():
            letters.append(char.lower())
            
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            palindrome = ''.join(combination)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)

    return palindromes
