
def palindromes_of_specific_lengths(str):
    str = str[18:99]
    palindromes = set()
    for len_pal in range(31, 52):
        for start in range(len(str)-len_pal+1):
            substr = str[start:start+len_pal]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes
