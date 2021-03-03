def bubble_sort(arr):
    
    arr_size = len(arr)

    for i in range(arr_size):
        for j in range(arr_size - i - 1):
            
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

def main():
    arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
    sorted_arr = bubble_sort(arr)
    print("Input  : ", arr) 
    print("Output : ", sorted_arr)

if __name__ == '__main__':
    main()

