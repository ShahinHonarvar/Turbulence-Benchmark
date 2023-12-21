
def filter_chars(string):
    result = ""
    for i in range(12, 78):
        if string[i].isalpha() and string[i] >= ":" and string[i] <= "L":
            result += string[i]
    return result
