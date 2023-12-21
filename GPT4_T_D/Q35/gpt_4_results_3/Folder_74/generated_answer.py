
def remove_repeat_chars(my_str):
    substring = my_str[70:97]
    freq = {}
    for char in substring:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1
    for char in freq:
        if freq[char] > 1:
            my_str = my_str.replace(char, '')
    return my_str
