def finder_method1(arr1:list, arr2:list):
    """
    Uses array index on sorted lists
    """
    arr1, arr2 = sorted(arr1), sorted(arr2)
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return arr1[i]

def finder_method2(arr1:list, arr2:list):
    """
    Uses zip function on sorted lists
    """
    arr1, arr2 = sorted(arr1), sorted(arr2)
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

print("Missing element is: ", finder_method2([1,2,3,4,3,5], [2,3,4,5,1]))
