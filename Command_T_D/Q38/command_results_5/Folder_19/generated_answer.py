def find_subset_of_length_n(s):
    return {*s, *{*s[i:j+1] for i in range(len(s)-12) for j in range(i+1, len(s))}}
