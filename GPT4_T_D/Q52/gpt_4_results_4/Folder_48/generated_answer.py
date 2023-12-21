
def palindrome_of_length_n(string):
    string = string.lower()
    results = set()
    for i in range(len(string)):
        for j in range(i+186, len(string)+1):
            if j-i == 186:
                substring = string[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    results.add(substring)
    return results
