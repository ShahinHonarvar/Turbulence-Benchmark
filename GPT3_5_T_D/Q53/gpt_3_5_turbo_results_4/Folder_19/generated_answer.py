
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 23, len(string) + 1):
            sub = string[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)

    return palindromes
