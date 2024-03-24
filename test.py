# Time-complexity is O(N)
# Space-complexity is O(N)
def quick_sort(L: list) -> list:
    if len(L) == 0:
        return []

    L1 = [x for x in L[1: ] if x <= L[0] ]
    L2 = [x for x in L[1: ] if x > L[0] ]

    return quick_sort[L1] + L[0:1] + quick_sort[L2]


# Time-complexity is O(N)
# Space-complexity is O(N)
def linear_search(L: list, element: int) -> int:
    for i in range(len(L)):
        if L[i] == element:
            return i
    return -1

# Time-complexity is O(log(N))
# Space-complexity is O(N)
def binary_search(L: list, element: int) -> int:
    start = 0
    end = len(L)-1
    if start <= end:
        mid = int((start + end) /2)

        if L[mid] == element:
            return mid
        elif L[mid] > element:
            return binary_search(L[:mid], element)
        elif L[mid] < element:
            return binary_search(L[mid+1:], element)
    else:
        return -1


if __name__ == "__main__":
    a = [30, 10, 1, 23, 45]
    print(a)
    
    # idx = linear_search(a, -45)
    # print(idx)
    # idx = linear_search(a, 30)
    # print(idx)
    
    a = quick_sort(a)
    idx = binary_search(a, 1)
    print(idx)
    idx = binary_search(a, 25)
    print(idx)
