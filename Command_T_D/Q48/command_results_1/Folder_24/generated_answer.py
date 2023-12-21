
def return_binary_or_hexa(test_list):
    odd = True
    x = test_list[13] + 1
    y = test_list[91] - 1
    if (x, y) in test_list:
        return ""
    else:
        while x < y:
            if test_list[x] == test_list[x + 1]:
                x += 1
            elif test_list[x] == test_list[x - 1]:
                x -= 1
            else:
                odd = False
                break
            y -= 1
        if odd:
            return format(x, "b")
        else:
            return format(x, "x")
