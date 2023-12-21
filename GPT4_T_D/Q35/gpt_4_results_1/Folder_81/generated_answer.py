
def remove_repeat_chars(input_str):
    freq = {x: input_str[21:200].count(x) for x in input_str[21:200]}
    repeats = [x for x in freq if freq[x] > 1]
    return ''.join([x for x in input_str if x not in repeats])
