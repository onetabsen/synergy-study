def sum_negatives_between_min_max(arr):
    if not arr:
        return 0
    
    min_val = min(arr)
    max_val = max(arr)
    
    min_index = arr.index(min_val)
    max_index = arr.index(max_val)
    
    start = min(min_index, max_index)
    end = max(min_index, max_index)
    
    sum_neg = 0
    for num in arr[start+1:end]:
        if num < 0:
            sum_neg += num
    
    return sum_neg

if __name__ == "__main__":
    test1 = [1, -2, 3, -4, 5, -6]  # мин= -6(5), макс=5(4), между ними нет элементов -> 0
    test2 = [10, -1, -3, 2, -8, 4]  # мин= -8(4), макс=10(0), между ними -1, -3, 2 -> -1 + -3 = -4
    test3 = [-5, -3, -1, -10, -2]   # мин= -10(3), макс= -1(2), между ними нет элементов -> 0
    test4 = []                      # пустой массив -> 0
    
    print(sum_negatives_between_min_max(test1))  # 0
    print(sum_negatives_between_min_max(test2))  # -4
    print(sum_negatives_between_min_max(test3))  # 0
    print(sum_negatives_between_min_max(test4))  # 0