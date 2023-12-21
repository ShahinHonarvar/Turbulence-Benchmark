
def return_nth_smallest_ascii(str):
    return next((i for i in str if ord(i) in range(ord(min(str)), 11)), str[0])
