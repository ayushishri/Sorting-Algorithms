def selection_sort(u):
    for j in range (0,len(u)-1,1):
        for i in range(j,len(u),1):
            if u[j]>u[i]:
                temp=u[j]
                u[j]=u[i]
                u[i]=temp
    return True

def merge_sort(u):
    mergeSort(u,0,len(u)-1)
    return True

def mergeSort(arr,l,r):
    if l < r:

        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+(r-1))/2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
def merge(arr,l,m,r):
    n1 = m - l + 1
    n2 = r- m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return True


def heapify(x):
    n=len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)
    return True

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
def reheapify(u,end):
    if (len(u)>0):
        i=0
        while True:
            if i>end:
                break
            l=i*2+1
            r=i*2+2
            if l>=end:
                break
            if r>=end:
                r=l
            if u[r]>=u[l]:
                n=r
            else:
                n=l
            if u[n]>u[i]:
                temp=u[i]
                u[i]=u[n]
                u[n]=temp
            i=n
        return True

def heap_sort(u):
    heapify(u)
    for i in range(len(u)-1,-1,-1):
        temp=u[i]
        u[i]=u[0]
        u[0]=temp
        reheapify(u,i)
    return True

