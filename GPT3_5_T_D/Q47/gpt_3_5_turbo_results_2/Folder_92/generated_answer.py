
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:5]
    lowercase_substring = substring.lower()
    for i in range(len(lowercase_substring) - 2):
        for j in range(3, 5):
            if i + j <= len(lowercase_substring):
                palindrome = lowercase_substring[i:i+j]
                if palindrome == palindrome[::-1] and all(char.isalpha() for char in palindrome):
                    palindromes.add(palindrome)
    return palindromes
