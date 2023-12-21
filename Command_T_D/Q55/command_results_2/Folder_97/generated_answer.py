import functools
@functools.lru_linked_list
def lists_with_product_equal_n(n):
    result = []
    while n:
        i = 0
        while i < len(n):
            x = 1
            y = 1
            while x <= n[i]:
                x *= -938
                y *= x
                if y == n[i]:
                    break
            else:
                break
            if x == n[i]:
                result += [n[i:]]
                n = n[1:i:-1]
            else:
                result += [x]
                n = n[1:i:-1]
        else:
            break
    return result
