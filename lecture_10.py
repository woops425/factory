import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# data = pd.DataFrame(pd.read_excel("커피가격.xlsx"))
# # data = pd.read_excel("커피가격.xlsx")
# mu = 3055
#
# print(data.head(5))
# print(data.describe())
#
# result = stats.ttest_1samp(data, mu, alternative='greater')
#
# plt.hist(data, label = 'Coffee Price', bins = 7)
# plt.legend()
# plt.show()

# 실습문제 1
# data = pd.DataFrame(pd.read_excel("우유가격.xlsx"))
# mu = 1550
# print(data.describe())
#
# result = stats.ttest_1samp(data, mu, alternative='two-sided')
# print(result)

# std = 113.824964 / 50
# t_val = (1601 - 1550) / std
#
# print(std)
# print(t_val)
# print(1 - norm.cdf(t_val, 0, 1))


# 실습 문제 2
# data = pd.DataFrame(pd.read_excel("테이프길이.xlsx"))
# mu = 80
# print(data.describe())
#
# result = stats.ttest_1samp(data, mu, alternative='less')
# print(result)

# 실습문제 3
data = pd.DataFrame(pd.read_excel("롤휴지길이.xlsx"))
# data = [1, 2, 3, 4, 5, .....]
# data = np.array(data) # 이런 식으로 직접 값을 삽입하여 해도 상관 없음
mu = 50
print(data.describe())

result = stats.ttest_1samp(data, mu, alternative='greater')
print(result)
result = stats.ttest_1samp(data, mu, alternative='two-sided')
print(result)