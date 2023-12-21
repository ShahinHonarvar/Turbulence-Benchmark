
def palindrome_of_length_at_least_n(string, n):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if j-i >= n:
                substr = string[i:j]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
