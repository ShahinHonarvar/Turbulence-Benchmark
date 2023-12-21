
def return_nth_smallest_ascii(string):
    count = {}
    for i in range(5):
        if string[i] in count:
            count[string[i]] += 1
        else:
            count[string[i]] = 1
    nth_smallest = min(count, key=count.get)
    return nth_smallest
