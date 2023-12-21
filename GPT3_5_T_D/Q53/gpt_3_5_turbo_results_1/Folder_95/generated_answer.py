
def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string) - 34):
        substring = string[i:i+35]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring.lower())
    return result
