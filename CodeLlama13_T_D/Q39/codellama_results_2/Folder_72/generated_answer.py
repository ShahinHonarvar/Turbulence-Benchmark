
def return_n_greatest_chars(string):
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return [char for char, count in sorted_chars[:37]]
