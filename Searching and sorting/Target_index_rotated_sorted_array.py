'''
Given a rotated sorted tuple, find the index of the target element
'''

def search(A, B, low=None, high=None):
    if A == []:
        return -1
    if low is None or high is None:
        low, high = 0, len(A)-1
    if low > high:
        return -1

    mid = (low + high) // 2

    if A[mid] == B:
        return mid

    if A[low] <= A[mid]:
        if B >= A[low] and A[mid] >= B:
            return search(A, B, low, mid-1)
        else:
            return search(A, B, mid+1, high)

    if B >= A[mid] and B <= A[high]:
        return search(A, B, mid+1, high)

    return search(A, B, low, mid-1)


test_cases = [(4, 5, 6, 7, 0, 1, 2), (0, 1, 2, 4, 5, 6, 7)]

for array in test_cases:
    print(array)
    for i in range(10):
        print(i, search(array, i))


arr = (3, 4, 5, 7, 9, 12, 15, 1)
print(arr)
for item in range(-5, 20):
    print('%3d : %5s'%(item, search(array, item)))
