
def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string)):
        for j in range(i + 97, min(i + 194, len(string) + 1)):
            substr = string[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result
