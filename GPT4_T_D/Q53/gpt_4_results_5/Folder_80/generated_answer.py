
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    results = set()
    for i in range(len(string)):
        for j in range(i + 30, len(string) + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                results.add(sub_string)
    return results
