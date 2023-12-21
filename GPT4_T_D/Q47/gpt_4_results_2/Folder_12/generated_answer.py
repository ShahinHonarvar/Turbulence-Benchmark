
def palindromes_of_specific_lengths(s):
    s = s.lower() 
    substring = s[62:89]
    palindromes = set()
    for i in range(0, len(substring)):
        for j in range(18, 22 if 21+i < len(substring) else len(substring)-(18+i)):
            fragment = substring[i:i+j]
            if fragment.isalpha() and fragment == fragment[::-1]:
                palindromes.add(fragment)
    return palindromes
