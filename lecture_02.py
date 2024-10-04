import numpy as np
import pandas as pd

# lst1 = [1,2,3,4,5]
# lst2 = [6,7,8,9,10]

# print(lst1)
# print(lst1 * 5) # lst1이 5번 반복되어 출력
# print(lst1 + lst2) # 리스트를 활용하는 경우, 단순 리스트 두 개가 합쳐진 형태로 출력됨
# print()

# a = np.array([1,2,3,4,5])
# b = np.array([6,7,8,9,10])

# print(arr1)
# print(arr1 * 5) # arr1의 인덱스 값들에 *5 된 값이 출력
# print(arr1 + arr2) # 배열을 활용하면, 리스트의 인덱스 값들의 합이 출력이 됨. 콤마도 제거되어 출력되는 것이 배열
# a = [[1,2], [3,4]]
# c = np.multiply(a, b)
# a = [['a','b','c'], ['d','e','f']]

# alist = [1,2,3,4,5]
# blist = [[10,20], [30,40],[50,60]]
# a = np.array(alist)
# b = np.array(blist)
# print(a)
# print(a[0][0]) # 1 // 0행 0열에 해당하는 값 : 1
# print(a[1][0]) # 3 // 1행 0열에 해당하는 값 : 3
# print(a*b) # 원소 연산
# print(np.dot(a,b)) # 행렬 연산
# print(a.min())
# print(shape(a))
# print(np.zeros((3,2), int))
# print(np.zeros((2,2),int))
# print(9*np.ones(2,int))

file_data = pd.read_excel("sample4.xlsx")
print(file_data[0:5])