'''
1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot

low  --> Starting index
high  --> Ending index
quickSort(arr[], low, high)
{
    if (low < high)
    {
        # pi is partitioning index, arr[pi] is now
        # at right place
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
'''
import random

class QuickSort:
    def partition(self, seq, left, right):
        i = left - 1
        pivot = seq[right]

        for j in range(left, right):
            if seq[j] < pivot:
                i += 1
                seq[i], seq[j] = seq[j], seq[i]

        seq[i+1], seq[right] = seq[right], seq[i+1]
        return i + 1

    def quicksort(self, seq, left, right):
        if left < right:
            p = self.partition(seq, left, right)

            self.quicksort(seq, left, p-1)
            self.quicksort(seq, p+1, right)

    
if __name__ == "__main__":
    seq = random.sample(range(100), 25)
    p = QuickSort()
    p.quicksort(seq, 0, len(seq)-1)
    print(seq)