def bubble_sort(arr):
    for i in range(len(arr)):
        swamped = False
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[i],arr[j] = arr[j], arr[i]
                swamped = True
        if swamped == False:
            break
    print(arr)


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    print(arr)

# insertion_sort([1,4,3,2])
def merge_sort(arr, start, end):

    def merge(arr1, arr2):

        ret = []
        for i in range(len(arr)):
             for j in range(i,len(arr)):
                if arr1[i] < arr2[j]:
                    ret.append(arr[i])
                    break
                else:
                    ret.append(arr[j])
                    continue
        return ret
    if start < end:
        middle = (end + start) // 2
        arr1 = merge_sort(arr, start, middle)
        arr2 = merge_sort(arr, middle+1, end)
        arr = merge(arr1, arr2)
    return arr


# print(merge_sort([1,4,3,2], 0 , 3))


def selection_sort(arr):
    for i in range(0,len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    # print(arr)
# selection_sort([1,8,3,9])

def quick_sort(arr):
    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot = partition(arr, low ,high) # arr[pi] is at the right place
            quick_sort_helper(arr, low, pivot-1)
            quick_sort_helper(arr, pivot+1, high)

    def partition(arr, low, high):
        i = low -1
        pivot = arr[high] # the last one
        for j in range(low,high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[j]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1



def counting_Sort(arr, k):
    counting = [0] * k+1
    for elem in arr:
        counting[elem] += 1
    index = 0
    for elem in range(len(counting)):
        while 0 < counting[elem]:
            arr[index] = elem
            index += 1
            counting[elem]-=1
    # n = len(arr)
    # quick_sort_helper(arr, 0, n-1)
    # print(arr)



def radix_sort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0,n):
        index = (arr[i]/exp1)
        count[index%10] +=1

    for i in range(1,10):
        count[i] += count[i-1]


def sorted_merge_not_Working(a:list,b:list):
    def switch(a_i,b_i):
        temp = a[a_i]
        a[a_i] = b[b_i]
        b[b_i] = temp
    b_index = 0
    for i in range(len(a)):
        if b_index <= len(b) and a[i] > b[b_index]:
            switch(i, b_index)
            if b_index + 1 < len(b):
                if b[b_index] > b[b_index + 1]:
                    switch(b[b_index], b[b_index+1])
                b_index += 1
    a.extend(b)
    print(a)

def sorted_merge(a,b):
    ret = []
    a_i = 0
    b_i = 0
    for _ in range(len(a)+len(b)):
        if b_i < len(b) and a[a_i] > b[b_i]:
            ret.append(b[b_i])
            b_i += 1
        else:
            ret.append(a[a_i])
            a_i += 1
    print(ret)

if __name__ == '__main__':
    sorted_merge_not_Working([1,3,5,6], [2,4])
    # pass
