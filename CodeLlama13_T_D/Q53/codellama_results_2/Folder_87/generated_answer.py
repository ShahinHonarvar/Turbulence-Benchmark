
def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i+18, len(string)+1):
            if string[i:j] == string[i:j][::-1]:
                result.add(string[i:j])
    return result
