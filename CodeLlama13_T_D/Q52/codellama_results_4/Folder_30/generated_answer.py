
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:i+94]
        if len(substr) == 94 and all(x.isalpha() for x in substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
