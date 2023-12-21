
def palindromes_of_specific_lengths(string):
    string = string[3:301]
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i+30, min(i+301, len(string)+1)):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
    return palindrome_set
