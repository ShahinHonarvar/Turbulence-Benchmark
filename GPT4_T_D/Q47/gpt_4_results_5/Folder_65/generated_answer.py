
def palindromes_of_specific_lengths(s):
    import re
    s = s[15:96].lower()
    palindromes = set()

    for i in range(20, 67):
        for j in range(len(s) - i + 1):
            sub = s[j:j+i]
            if sub == sub[::-1]:
                check = re.match("^[A-Za-z]*$", sub)
                if check is not None:
                    palindromes.add(sub)
    return palindromes
