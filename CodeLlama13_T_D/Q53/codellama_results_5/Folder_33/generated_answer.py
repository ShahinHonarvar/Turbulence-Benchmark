
def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) - 139):
            if string[i:j] == string[j - 1:-1]:
                result.add(string[i:j])
    return result
