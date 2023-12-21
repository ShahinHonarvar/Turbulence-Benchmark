
def palindromes_of_specific_lengths(string):
    string = string[18:88]
    result = set()
    for len_of_palindrome in range(38, 61):
        for i in range(0, len(string) - len_of_palindrome + 1):
            substring = string[i:i+len_of_palindrome]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result
