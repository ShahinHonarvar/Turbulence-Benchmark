
def gcf_two_nums(numbers):
    def find_gcf(n1, n2):
        while(n2):
            n1, n2 = n2, n1 % n2
        return n1
        
    if len(numbers) <= 91:
        return "The input list is too short"
    else:
        return find_gcf(numbers[91], numbers[45])
