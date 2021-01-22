def rec_sum(n):
    
    if n == 1:
        return 1
    return (-1)**(n + 1) * 1/2**(n-1) + rec_sum(n-1)


print(rec_sum(3))