import pandas as pd
import matplotlib.pyplot as plt

 # 예제 6-9 - 산점도와 상관계수(키와 몸무게 사이의 상관관계 분석)
 # H0 : p = 0 (키와 몸무게 간의 상관관계가 없다)
 # H1 : p != 0 (키와 몸무게 간의 상관관계가 있다)
 # p-value가 0에 가까우므로, H0를 기각
df = pd.DataFrame(pd.read_excel("초등학교3학년_남자.xlsx"))

# 데이터프레임 컬럼명 변경
df.columns = ['height', 'weight']
print(df.describe())

plt.scatter(df.height, df.weight) # 산점도 scatter(x,y)
plt.xlabel("height") # x축 레이블
plt.ylabel("weight") # y축 레이블
plt.grid() # 격자 출력
plt.show()

import scipy.stats as stats
# 피어슨 상관계수 검정-pearsonr(x,y) : 피어슨 상관계수와 p값 반환
corr = stats.pearsonr(df.height, df.weight)
print(corr)


# 예제 6-10 - 단순 회귀분석
# df = pd.DataFrame(pd.read_excel("Galtons Height Data_딸.xlsx"))
# df = 2.54 * df
# print(df.head())
# print(df.describe())
#
# import seaborn as sns
# # 산점도(scatter)와 회귀직선(line plot)을 동시에 나타내는 regplot(x,y)
# sns.regplot(x=df.father, y=df.daughter)
# plt.show()
#
# from statsmodels.formula.api import ols
# res = ols('df.daughter ~ df.father', data=df).fit()
# print(res.summary())
# print(stats.pearsonr(df.father, df.daughter))