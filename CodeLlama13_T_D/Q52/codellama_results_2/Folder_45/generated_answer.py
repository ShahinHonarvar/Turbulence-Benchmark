
def palindrome_of_length_n(string):
    # find all palindromes of length 21 in the string
    palindromes = set()
    for i in range(len(string) - 20):
        substr = string[i:i+21]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
