
def palindromes_of_specific_lengths(s):
    from string import ascii_letters
    palindromes = set()

    s = s[22:96].lower()
    for i in range(len(s)):
        for j in range(i+52, min(i+56, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and set(substring).issubset(ascii_letters):
                palindromes.add(substring)

    return palindromes
