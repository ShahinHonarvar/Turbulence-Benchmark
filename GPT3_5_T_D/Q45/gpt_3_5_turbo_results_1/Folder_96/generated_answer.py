
def palindromes_between_indices(string):
    import itertools
    from collections import Counter

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    letters = [c.lower() for c in string[3:9] if c.isalpha()]
    letter_counts = Counter(letters)

    all_permutations = set()
    for perm in itertools.permutations(letters, len(letters)):
        palindromes = []
        for i in range(len(perm)//2 + 1):
            if perm[i] != perm[-i-1]:
                break
        else:
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                all_permutations.add(palindrome)

    return all_permutations
