import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
import scipy.stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import seaborn as sns

# 문제 1)
# data = {
#     'distance': [11.4, 11.7, 11.6, 13.1, 12.9, 13.2, 13.6, 13.5, 13.5],
#     'oil': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
#     'engine': ['engine1', 'engine1', 'engine1', 'engine2', 'engine2', 'engine2', 'engine3', 'engine3', 'engine3']
# }
# df = pd.DataFrame(data)
#
df = pd.DataFrame(pd.read_excel('hw4_1.xlsx'))

df.columns = ['distance', 'engine', 'oil']
print(df)
# 이원분산분석 모델 생성
model = ols('distance ~ C(oil) + C(engine)', data=df).fit()
print("이원분산분석")
print(anova_lm(model))

# 사후 다중비교 (Tukey HSD)
print("Tukey-Oil:")
tukey_oil = pairwise_tukeyhsd(df['distance'], df['oil'], alpha=0.05)
print(tukey_oil)

print("Tukey-Engine:")
tukey_engine = pairwise_tukeyhsd(df['distance'], df['engine'], alpha=0.05)
print(tukey_engine)


# 문제 2
# df = pd.DataFrame(pd.read_excel("hw4_2.xlsx"))
# print(df.describe())
#
# import scipy.stats as stats
# # 피어슨 상관계수 검정-pearsonr(x,y) : 피어슨 상관계수와 p값 반환
# corr = stats.pearsonr(df.temp, df.rain)
# print(corr)
#
# res = ols('df.rain ~ df.temp', data=df).fit()
# print(res.summary())
# print(stats.pearsonr(df.temp, df.rain))