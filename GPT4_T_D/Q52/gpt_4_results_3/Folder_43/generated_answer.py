
def palindrome_of_length_n(string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    string = string.lower()
    results = set()
    for start in range(len(string)):
        for end in range(start + 51, len(string) + 1):
            substring = string[start:end]
            if all(c in alphabet for c in substring):
                if substring == substring[::-1]:
                    results.add(substring)
    return results
