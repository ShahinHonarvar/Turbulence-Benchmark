
def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    substring = string[119:257]
    substring = substring.lower()
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i:i+length][::-1] and substring[i:i+length].isalpha():
                palindrome_set.add(substring[i:i+length])
    return palindrome_set
