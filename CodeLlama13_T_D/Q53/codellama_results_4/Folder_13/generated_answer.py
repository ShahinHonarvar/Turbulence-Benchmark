
def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substr = string[i:j]
            if len(substr) < 52:
                continue
            if substr == substr[::-1]:
                result.add(substr)
    return result
