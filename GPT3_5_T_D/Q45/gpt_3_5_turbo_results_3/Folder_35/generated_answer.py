
def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, 5):
        for combo in combinations(letters, i):
            palindrome = "".join(combo)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)
    return palindromes
