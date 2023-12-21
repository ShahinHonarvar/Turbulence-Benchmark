
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(36, len(string)+1):
        for j in range(len(string)-i+1):
            substr = string[j:j+i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
