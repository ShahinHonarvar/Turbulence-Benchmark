
def palindromes_between_indices(string):
    import itertools
    import re
    from string import ascii_letters

    letter_combinations = itertools.permutations(re.findall(r'[a-zA-Z]', string[:6].lower()))

    palindromes = set()
    for combination in letter_combinations:
        letters = ''.join(combination)
        palindrome = letters + letters[::-1]
        if len(palindrome) >= 6:
            palindromes.add(palindrome)

    return palindromes
