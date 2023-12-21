
def palindromes_of_specific_lengths(string):
    import re
    result = set()
    search_string = re.sub('[^A-Za-z]', '', string[28:94]).lower()
    for length in range(38, 50):
        for i in range(len(search_string) - length + 1):
            substring = search_string[i:i+length]
            if substring == substring[::-1]:
                result.add(substring)
    return result
