'''
1. split the origin sequence to half until there is only one element in each sub-sequence
2. the base case (one element) is already sorted
3. backtracking, compare the elements in the left and right half sequence, and merge
4. repeat till all the subsequences merged to a completed one
'''
import random

class MergeSort:
    def merge(self, seq, left, mid, right):
        '''
        merge two sub sequences
        first is seq[left:mid]
        second is seq[mid:right]
        '''
        n1 = mid - left + 1
        n2 = right - mid

        LeftSeq = seq[left:mid+1]
        RightSeq = seq[mid+1:right+1]

        # merge the two sub sequence back into the seq[left:right]
        i, j = 0, 0
        k = left

        while i < n1 and j < n2:
            # move the index of the smaller element to the right 
            if LeftSeq[i] <= RightSeq[j]:
                seq[k] = LeftSeq[i]
                i += 1
            else:
                seq[k] = RightSeq[j]
                j += 1
            k += 1
        
        # keep add the remaining elements in LeftSeq or RightSeq 
        # if there are any
        while i < n1:
            seq[k] = LeftSeq[i]
            i += 1
            k += 1
        while j < n2:
            seq[k] = RightSeq[j]
            j += 1
            k += 1
        
    def mergesort(self, seq, left, right):
        if left < right:
            mid = (left + right) // 2
            self.mergesort(seq, left, mid)      # split on the left
            self.mergesort(seq, mid+1, right)   # split on the right
            self.merge(seq, left, mid, right)   # sort and merge

if __name__ == "__main__":
    seq = random.sample(range(1,100), 25)
    p = MergeSort()
    p.mergesort(seq, 0, len(seq)-1)
    print(seq)