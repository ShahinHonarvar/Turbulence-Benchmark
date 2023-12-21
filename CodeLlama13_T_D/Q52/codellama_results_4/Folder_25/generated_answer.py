
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:i+90]
        if len(substr) != 90:
            continue
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
