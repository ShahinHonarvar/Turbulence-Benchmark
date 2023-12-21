
def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        substr = string[i:]
        if len(substr) < 73:
            continue
        if substr == substr[::-1]:
            result.add(substr)
    return result
