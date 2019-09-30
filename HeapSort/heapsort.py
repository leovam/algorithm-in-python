'''
Input data: 4, 10, 3, 5, 1
         4(0)
        /   \
     10(1)   3(2)
    /   \
 5(3)    1(4)

The numbers in bracket represent the indices in the array 
representation of data.

Applying heapify procedure to index 1:
         4(0)
        /   \
    10(1)    3(2)
    /   \
5(3)    1(4)

Applying heapify procedure to index 0:
        10(0)
        /  \
     5(1)  3(2)
    /   \
 4(3)    1(4)
The heapify procedure calls itself recursively to build heap
 in top down manner.
'''

import random

class HeapSort:
    def heapify(self, seq, n, i):
        largest = i                        # initialize largest as root
        L = 2 * i + 1                      # left index
        R = 2 * i + 2                      # right index
        if L < n and seq[i] < seq[L]:
            largest = L
        
        if R < n and seq[largest] < seq[R]:
            largest = R
        
        if largest != i:
            seq[i], seq[largest] = seq[largest], seq[i]

            self.heapify(seq, n, largest)
    
    def heapsort(self, seq):
        n = len(seq)

        for i in range(n, -1, -1):
            self.heapify(seq, n, i)
        
        for i in range(n-1, 0, -1):
            seq[i], seq[0] = seq[0], seq[i]
            self.heapify(seq, i, 0)


if __name__ == '__main__':
    seq = random.sample(range(100), 25)
    p = HeapSort()
    p.heapsort(seq)
    print(seq)
    