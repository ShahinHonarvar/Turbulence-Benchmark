
def return_n_greatest_chars(string):
    char_count = {}
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    sorted_chars = sorted(char_count.items(), key=lambda x: x[0], reverse=True)
    return sorted_chars[:28]
