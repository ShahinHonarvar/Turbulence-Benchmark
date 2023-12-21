
def palindromes_between_indices(string):
    from itertools import permutations
    import string as s

    english_letters = [c.lower() for c in s.ascii_letters]
    substr = string[3:8].lower()
    palindromes = set()

    for arrangement in permutations(substr, len(substr)):
        if len(set(arrangement) - set(english_letters)) == 0:
            palindrome = ''.join(arrangement)
            if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                palindromes.add(palindrome)

    return palindromes
