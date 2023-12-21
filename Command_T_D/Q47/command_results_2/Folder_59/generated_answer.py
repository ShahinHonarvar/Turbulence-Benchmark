def palindromes_of_specific_lengths(s):
    i = 0
    while i < len(s):
        j = s[i:].rfind(s[i][::-1])
        if j != -1:
            yield s[i:j+1][::-1]
            i = j + 1
        else:
            i += 1
    yield s[i:][::-1]
