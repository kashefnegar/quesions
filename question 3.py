def mergeFunction(list1 , list2):
    size_1 = len(list1)
    size_2 = len(list2)

    result = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    return result + list1[i:] + list2[j:]

if __name__ == "__main__":  
    test_list1 = [1, 5, 6, 9, 11]
    test_list2 = [3, 4, 7, 8, 10]

    print(mergeFunction(test_list1, test_list2))
