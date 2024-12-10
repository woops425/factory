import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import seaborn as sns
import scipy.stats as stats
from scipy.stats import chisquare
from scipy.stats import  chi2_contingency

excel_name = "data_202010629_박상우.xlsx"
# Q1 code here
df1 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q1")
print(df1)
obs = pd.DataFrame({'line1': [11,28,44,17], 'line2': [25, 31, 34,10],'line3': [27, 15, 42,16]})
obs.index=['결점A', '결점B', '결점C','결점D']
print(obs)
from scipy.stats import  chi2_contingency
result = chi2_contingency(obs, correction = False)
print(result)

# Q2 code here
df2 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q2")

mu = 55000
print(df2.describe())
result = stats.ttest_1samp(df2, mu, alternative='greater')
print(result)

# Q3 code here
df3 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q3")
mu = 75
print(df3.describe())

result = stats.ttest_1samp(df3, mu, alternative='two-sided')
print(result)

# Q4 code here
df4 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q4")
model = ols('earn ~ C(team) + C(time)', data=df4).fit()
print(anova_lm(model))
print()
print(pairwise_tukeyhsd(df4['earn'], df4['team'], alpha=0.05))
print()
print(pairwise_tukeyhsd(df4['earn'], df4['time'], alpha=0.05))

# Q5 code here
df5 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q5")
result = stats.ttest_ind(df5.original, df5.new, alternative='two-sided')
print(result)

# Q6 code here
# 과일 종류는 type, 비료는 use, 당도는 brix로 설정
df6 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q6")
model = ols('brix ~ C(type) + C(use) + C(type):C(use)', data=df6).fit()
print(model)
print(anova_lm(model))
print()
tukey = pairwise_tukeyhsd(df6['brix'], df6['type'], alpha=0.05)
print(tukey)
print()
tukey = pairwise_tukeyhsd(df6['brix'], df6['use'], alpha=0.05)
print(tukey)

################### Put your final exam answer here #####################################
# 1번 정답
# 가설
# H0: 생산라인 별로 결함부분에 차이가 없다.
# H1: 생산라인 별로 결함부분에 차이가 있다.
# p값 : 0.011
# 기각여부 : H0를 기각한다
# 결론 : 생산라인 별로 결함 부분에 차이가 있다는 주장에 타당한 근거가 있다.

# 2번 정답
# 가설
# H0: 모집단 평균은 55000이다.
# H1: 모집단 평균은 55000보다 크다.
# p값 : 0.2797
# 기각여부 : H0를 기각하지 않는다.
# 결론 : B사가 주장한 월 휴대전화 사용료가 55,000원이라는 주장은 유의미하다.

# 3번 정답
# 가설
# H0: 보충학습 전과 후의 영어성적에는 차이가 없다.
# H1: 보충학습 전과 후의 영어성적에는 차이가 있다.
# p값 : 0.1837
# 기각여부 : H0를 기각하지 않는다.
# 결론 : 보충학습 전과 후의 영어성적에는 유의미한 차이가 없다.

# 4번 정답
# 부서별 차이에 대한 가설
# H0: 5개의 부서에 따른 실적의 평균은 차이가 없다.
# H1: 적어도 한 개 부서의 평균은 나머지와 다르다.
# p값 : 0.0089
# 기각여부 : H0를 기각한다
# 결론 : 적어도 한 개 부서의 평균은 나머지와 다르다.

# 분기별 차이에 대한 가설
# H0: 4개의 분기에 따른 실적의 평균은 차이가 없다.
# H1: 적어도 한 개 분기의 평균은 나머지와 다르다.
# p값 : 0.2780
# 기각여부 : H0를 기각할 수 없다.
# 결론 : 4개 분기에 따른 실적의 평균은 차이가 없다.
# 부서별 차이에 대한 가설에서 H0가 기각되었기 때문에, 어떤 부서끼리의 차이가 있는지 확인한 결과,
# B부서와 C부서, C부서와 D부서, 그리고 C부서와 E부서 간의 차이가 있는 걸로 확인되었다.
# B부서의 실적이 C부서보다 높다
# D부서의 실적이 C부서보다 높다
# E부서의 실적이 C부서보다 높다

# 5번 정답
# 가설
# H0: 기존 키보드와 새로운 키보드의 분당 단어수는 차이가 없다
# H1: 기존 키보드와 새로운 키보드의 분당 단어수는 차이가 있다
# p값 : 0.253
# 기각여부 : H0를 기각하지 않는다
# 결론 : 기존 키보드와 새로운 키보드의 분당 단어수는 차이가 없다는 충분한 근거를 제시한다

# 6번 정답
# 비료의 차이에 따른 가설
# H0: 3개의 비료에 따른 당도의 차이는 없다.
# H1: 적어도 하나의 비료에 대한 당도의 평균은 나머지와 다르다.
# p값 : 5.22e-12
# 기각여부 : H0를 기각한다.
# 결론 : 적어도 하나의 비료에 대한 당도의 평균은 나머지와 다르다.
# 어떤 비료 간의 당도 차이가 있는지에 대해 알아보기 위해 사후검정을 한 결과,
# A 비료와 C 비료 간에 과일의 당도 차이가 유의미한 것으로 밝혀졌다.
# A비료와 C비료 간의 당도 차이가 있다는 걸 알 수 있고, C비료를 이용했을 때 과일의 당도가 더 높다는 것을 확인할 수 있다.

# 과일 종류의 차이에 따른 가설
# H0: 3개의 과일에 따른 당도 차이에 대한 당도의 차이는 없다.
# H1: 적어도 하나의 과일에 대한 당도의 평균은 나머지와 다르다.
# p값 : 1.038e-15
# 기각여부 : H0를 기각한다.
# 결론 : 적어도 하나의 과일에 대한 당도의 평균은 나머지와 다르다.
# 어떤 과일이냐에 따라 당도 차이가 있는지를 알아보기 위해 사후검정을 한 결과,
# 포도와 복숭아 간의 당도 차이가 유의미하며, 복숭아와 수박 간의 당도 차이가 유의미한 것으로 밝혀졌다.
# 포도가 복숭아보다 당도가 높고, 수박이 복숭아보다 당도가 높다는 것을 확인할 수 있다.

