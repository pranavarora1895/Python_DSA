def bin_search(list_data, target, low_val, high_val):
    list_data.sort()
    print(list_data)
    mid = (high_val + low_val) // 2
    if target == list_data[mid]:
        return mid
    else:
        if target > list_data[mid]:
            return bin_search(list_data, target, mid + 1, high_val)
        elif target < list_data[mid]:
            return bin_search(list_data, target, low_val, mid - 1)


if __name__ == '__main__':
    data = [34, 45, 66, 12, 23, 78, 22, 11, 4]
    low = 0
    high = len(data) - 1
    pos = bin_search(data, 23, low, high)
    print(pos)