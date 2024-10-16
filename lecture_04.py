import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import describe

# data = pd.read_excel("중학생_남자_몸무게.xlsx")
# print(data[0:5])
# 평균 계산
# print("평균값 = ", np.average(data), "\n")
# # 중앙값 계산
# print("중앙값 = ", np.median(data))
# print("중앙값 = ", data.median(), "\n")
# # 최빈값 계산
# print("최빈값(mode) = ", stats.mode(data))
# print("최빈값 : ", data.mode())

# data = [13,14,15,16,17]
# print(stats.tvar(data))
# data2 = [5,10,15,20,25]
# print(stats.tvar(data2))

data = pd.DataFrame(pd.read_excel("외식비.xlsx"))
print("평균")
print(np.mean(data, axis=0))

print("범위 range")
print(np.max(data, axis=0)-np.min(data, axis=0))
print()

print("분산 variance")
print(np.var(data, axis=0))
print()
# data = pd.DataFrame(pd.read_excel("외식비_3개.xlsx"))
# print(data.describe())
# print(stats.describe(data))

