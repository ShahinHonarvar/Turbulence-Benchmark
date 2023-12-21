
def palindromes_between_indices(string):
    import itertools
    import string as s
  
    string = string.lower()

    letters = []
    for index, char in enumerate(string):
        if 0 <= index <= 7 and char in s.ascii_letters:
            letters.append(char)
  
    palindromes = []
    for p in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.append(palindrome.lower())

    return set(palindromes) if len(palindromes) > 0 else set()
