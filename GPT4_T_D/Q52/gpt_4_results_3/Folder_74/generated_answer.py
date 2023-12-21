
def palindrome_of_length_n(string):
    string = string.lower()
    result_set = set()
    for i in range(len(string) - 95):
        substring = string[i:i+96]
        if substring == substring[::-1] and substring.isalpha():
            result_set.add(substring)
    return result_set
