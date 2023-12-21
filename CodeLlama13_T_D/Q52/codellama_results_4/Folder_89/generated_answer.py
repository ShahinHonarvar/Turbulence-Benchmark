
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:i+37]
        if len(substr) != 37:
            continue
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
