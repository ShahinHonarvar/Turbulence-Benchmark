
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
