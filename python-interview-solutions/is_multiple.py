

def sum_sqr(k):
    return sum([val*val for val in range(1, k, 2)])

if __name__ == '__main__':
    result = sum_sqr(10)
    print(result)
    
