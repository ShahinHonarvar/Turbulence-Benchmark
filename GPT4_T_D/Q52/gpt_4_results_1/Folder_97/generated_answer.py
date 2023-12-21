
def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string)-209):
        substring = string[i:i+210]
        if all(ch.isalpha() for ch in substring) and substring==substring[::-1]:
            result.add(substring)
    return result
