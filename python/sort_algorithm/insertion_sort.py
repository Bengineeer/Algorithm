def insertion_sort(arr):

    for i in range(len(arr) - 1):
        target = arr[i+1]

        sorted_value = [:i+1]
        num = 0
        while num < i: 
            if arr[num] < target:

            num += 1
            
def main():
    arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
    sorted_arr = insertion_sort(arr)
    print("Input  : ", arr)
    print("Output : ", sorted_arr)

if __name__ == '__main__':
    main()
