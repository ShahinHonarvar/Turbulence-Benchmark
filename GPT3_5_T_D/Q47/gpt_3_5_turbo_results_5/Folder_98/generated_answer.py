
def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    substring = string[:21].lower()
    for length in range(5, 81):
        for start in range(len(substring) - length + 1):
            end = start + length
            sub_palindrome = substring[start:end]
            if sub_palindrome == sub_palindrome[::-1] and sub_palindrome.isalpha():
                palindrome_set.add(sub_palindrome)
    return palindrome_set
