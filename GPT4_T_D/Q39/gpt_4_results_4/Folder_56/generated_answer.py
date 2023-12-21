
def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x), reverse=True)
    return sorted(sorted_s[:21])
