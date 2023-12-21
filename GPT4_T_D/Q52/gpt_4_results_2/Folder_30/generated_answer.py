
def palindrome_of_length_n(str):
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        for j in range(i+94, len(str)+1):
            substr = str[i:j]
            if substr == substr[::-1] and all(c.isalpha() for c in substr):
                palindromes.add(substr)
    return palindromes
