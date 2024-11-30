# import numpy as np
import pandas as pd
from scipy import stats

# 예제 6-2
# data = pd.read_excel("성인_스마트폰_이용시간.xlsx")
# print(data.describe())
#
# from matplotlib import pyplot as plt
#
# # 수평의 상자 도형(False의 F는 대문자로)
# data.boxplot(column=["male", "female"], vert=False)
# # plt.show()
#
# # d1 = data.male
# # d2 = data.female.dropna()
# # result = stats.ttest_ind(d1, d2)
# d1 = pd.read_excel("성인_스마트폰_이용시간_남자.xlsx")
# d2 = pd.read_excel("성인_스마트폰_이용시간_여자.xlsx")
# result = stats.ttest_ind(d1.male, d2.female, alternative='less')
# print(result)
#
# # H0 : u_male = u_female
# # H1 : u_male > u_female

# 예제 6-3
# data = pd.read_excel("대학생_수면시간.xlsx")
# a1 = pd.read_excel("성인_스마트폰_이용시간_남자.xlsx") # 등분산 연습문제
# a2 = pd.read_excel("성인_스마트폰_이용시간_여자.xlsx")
#
# b1 = pd.read_excel("대학생_수면시간_남자.xlsx") # 이분산 연습문제
# b2 = pd.read_excel("대학생_수면시간_여자.xlsx")
#
# result1 = stats.levene(a1.male, a2.female, center='mean')
# result2 = stats.levene(b1.male, b2.female, center='mean')
# result1 = stats.ttest_ind(d1.male, d2.female, equal_var="False")
# result2 = stats.ttest_ind(d1.male, d2.female, equal_var="True")
# print(result1) # pvalue = 0.4929 => H0 가설을 기각할 수 없고, 분산이 같다(등분산)
# print(result2) # pvalue = 3.19e-06 => H0 가설을 기각하고, 분산에 차이가 있다(이분산)

# ------------------------------------------(독립된 표본에 대한 예제였음)

# 예제 6-5(대응표본)
data = pd.read_excel("피트니스_결과.xlsx")
print(data.describe())

from matplotlib import pyplot as plt
plt.boxplot([data.before, data.after], vert=False)
# plt.show()

result = stats.ttest_rel(data.before, data.after, alternative='greater')
print(result)