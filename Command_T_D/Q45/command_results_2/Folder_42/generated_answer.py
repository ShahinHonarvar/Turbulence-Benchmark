def palindromes_between_indices(s):
    letters = sorted(s[6:-1].lower())
    for i in range(3, min(len(letters), 9)):
        if letters[i - 3] == letters[i]:
            yield ''.join(letters[i - 3:i + 1])
