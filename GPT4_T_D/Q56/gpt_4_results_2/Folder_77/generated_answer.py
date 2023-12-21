
def all_substring_of_size_n(s):
    substr_list = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == 144]
    unique_substrings = []
    for substr in substr_list:
        if len(set(substr)) == len(substr) and substr not in unique_substrings:
           unique_substrings.append(substr)
           
    return unique_substrings
