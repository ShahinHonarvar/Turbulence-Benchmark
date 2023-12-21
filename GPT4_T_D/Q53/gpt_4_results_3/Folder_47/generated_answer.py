
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i+77, len(string)+1):
            chunk = string[i:j]
            if chunk == chunk[::-1] and chunk.isalpha():
                palindrome_set.add(chunk)
    return palindrome_set
