def binarysearch(list, item):
    l = 0
    u = len(list) -1
    while l <= u:
        mid = (l + u) // 2
        if item == list[mid]:
            return "found in position" + str(mid)
        if item < list[mid]:
            u = mid - 1
        else:
            l = mid + 1
    return "not found"
            

list1 = [1,2,3,4,5,6,7]
item1 = 2
finding = binarysearch(list1, item1)
print(finding)


