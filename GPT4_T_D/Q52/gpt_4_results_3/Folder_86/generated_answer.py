
def palindrome_of_length_n(string):
    string = string.lower()
    result_set = set()
    for i in range(len(string)):
        end = i + 181
        if end > len(string):
            break
        substring = string[i:end]
        if substring == substring[::-1] and substring.isalpha():
            result_set.add(substring)
    return result_set
