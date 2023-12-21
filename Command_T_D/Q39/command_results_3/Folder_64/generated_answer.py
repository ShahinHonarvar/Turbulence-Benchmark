def return_n_greatest_chars(str_input):
    return [c for c in sorted(str_input, key=lambda x: ord(x), reverse=True)[:39]]
