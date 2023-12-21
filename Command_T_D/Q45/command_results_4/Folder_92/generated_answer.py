def palindromes_between_indices(str):
    letters = str[4:7]
    for i in range(len(letters)):
        yield letters[:i] + letters[i:-i] + letters[i+1:]
    for i in range(len(letters)):
        yield letters[:i] + letters[i:-i] + letters[i+1:]
