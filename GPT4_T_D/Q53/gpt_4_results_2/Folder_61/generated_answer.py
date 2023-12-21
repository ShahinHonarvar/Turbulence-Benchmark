
def palindrome_of_length_at_least_n(str):
    str = str.lower()
    str = "".join(e for e in str if e.isalnum())
    pal_set = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            curr_str = str[i:j + 1]
            if len(curr_str) >= 5 and curr_str == curr_str[::-1]:
                pal_set.add(curr_str)
    return pal_set
