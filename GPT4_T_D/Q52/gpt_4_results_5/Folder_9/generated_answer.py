
def palindrome_of_length_n(string):
    result_set = set()
    string = string.lower()
    for start in range(len(string)):
        for end in range(start, len(string)):
            sub_str = string[start:end+1]
            if len(sub_str) == 72 and sub_str == sub_str[::-1] and sub_str.isalpha():
                result_set.add(sub_str)
    return result_set
