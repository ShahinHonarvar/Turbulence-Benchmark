
def palindrome_of_length_at_least_n(string, n):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                if j - i >= n:
                    palindromes.add(string[i:j])
    return palindromes
