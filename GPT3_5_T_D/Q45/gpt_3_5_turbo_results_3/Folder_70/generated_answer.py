
def palindromes_between_indices(string):
    letters = []
    for ch in string[1:7]:
        if ch.isalpha():
            letters.append(ch.lower())
    
    palindromes = set()
    if len(letters) >= 4:
        from itertools import permutations
        for perm in permutations(letters, 4):
            palindrome = "".join(perm)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)

    return palindromes
