
def composite_nums_between_indices(num_list):
    def isComposite(n):
        if n <= 1:
            return False
        if n == 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    return {num for num in num_list[50:201] if isComposite(num)}
