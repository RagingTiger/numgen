"""
n = number of elements
k = number of combined elements
"""

# functions
def recurse_factory(level, n):
    def recurse_combi(number, k):
        # check level
        if k is level:
           print(number)
           return
        
        # start recurse
        for i in range(n):
            recurse_combi(number[:k-1] + str(i) + number[k:], k - 1)

    # return factory recurse function
    return recurse_combi       

def numgen(n, k):
    # initial setup
    start = ''.join(list('0' * k))

    # build recurse
    recurse = recurse_factory(0, n)
    
    # start recurse
    recurse(start, k)


# executable
if __name__ == '__main__':
    import sys
    numgen(int(sys.argv[1]), int(sys.argv[2]))
