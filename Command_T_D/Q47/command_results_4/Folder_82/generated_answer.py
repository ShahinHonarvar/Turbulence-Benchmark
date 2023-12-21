def palindromes_of_specific_lengths(text):
    letters = set(str.lower(text[3:]))
    return {
        s[::-1]
        for s in [
            s[3:300]
            for s in text[3:-1].split()
            if s.isalpha() and set(s) <= letters
        ]
    }
