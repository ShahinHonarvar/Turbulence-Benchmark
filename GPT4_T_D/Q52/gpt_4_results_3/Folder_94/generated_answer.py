
def palindrome_of_length_n(string):
    substring_set = set()
    string = string.lower()

    for i in range(len(string)):
        for j in range(i + 93, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and all(char.isalpha() for char in substring):
                substring_set.add(substring)

    return substring_set
