
def return_binary_or_hexa(test_tup):
    a, b = test_tup[18], test_tup[60]
    if a + 1 <= b - 1:
        curr = a + 1
        curr_sum = 0
        while curr < b:
            curr_sum += curr
            curr += 1
        if curr_sum % 2 == 0:
            return hex(curr_sum)
        else:
            return f'0b{curr_sum}'
    else:
        return ''
