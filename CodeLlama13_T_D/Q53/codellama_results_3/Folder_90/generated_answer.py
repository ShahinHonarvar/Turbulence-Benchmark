
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 139):
        substr = string[i:i+140]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
