import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
import scipy.stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import seaborn as sns

# 예제 6-6 일원 분산분석- 한 개의 요인에 대해 3개 이상의 평균을 비교할 때 사용 : f_oneway(sample1, ..., sampleN)
# H0 : 세 가지 비료에 따른 수확량의 평균에는 차이가 없다
# H1 : 적어도 한 개의 비료의 평균은 나머지와 다르다
a = [25, 29, 27, 23, 22, 25]
b = [34, 36, 38, 32, 35, 35]
c = [29, 31, 27, 26, 25, 27]

# 동시 신뢰구간을 이용한 다중비교(H0가 기각되었을 때, H1의 여러 케이스 중 어느 케이스에 해당하는지 알기 위함)
# pairwise_tukeyhsd()
# tukeyhsd를 사용하기 위해선 세로 형태의 DataFrame 형태로 변환이 필요함
# df = pd.DataFrame({'product': a+b+c, 'group':np.repeat(['a', 'b', 'c'], repeats=6)})
# print(df)
# print(f_oneway(a,b,c))
#
# result = pairwise_tukeyhsd(df['product'],df['group'],alpha=0.05)
# print(result)
#
# print(scipy.stats.f_oneway(a,b,c))
# print(scipy.stats.ttest_ind(a,b))
# print(scipy.stats.ttest_ind(a,c))
# print(scipy.stats.ttest_ind(b,c))
#
# print('a mean = ', np.mean(a), ', a std = ', np.std(a))
# print('b mean = ', np.mean(a), ', b std = ', np.std(b))
# print('c mean = ', np.mean(a), ', c std = ', np.std(c))

# # 예제 6-7 반복이 없는 이원 분산분석(요인이 2개) - 요인이 2개이니 가설도 2개
# df = pd.read_excel("이원분석_주행거리.xlsx")
# # ols 함수에는 독립변수(영향을 주는 변수) 앞에 C를 붙여줘야함
# # ex) model = ols('종속변수column ~ C(독립변수1column) + C(독립변수2column)', DataFrame).fit()
# model = ols('distance ~ C(road) + C(car)', data=df).fit()
# print(anova_lm(model))
#
# # Tukey's test
# print()
# print(pairwise_tukeyhsd(df['distance'], df['road'], alpha=0.05))
# print()
# print(pairwise_tukeyhsd(df['distance'], df['car'], alpha=0.05))


# 예제 6-8 반복이 있는 이원 분산분석 - 요인a에 대한 가설 / 요인 b에 대한 가설/ 요인a와 요인b의 교호작용에 따른 차이에 대한 가설
# H0 : 평균이 모두 같다. 다르지 않다.
# H1 : 적어도 한 개의 평균은 나머지와 다르다.
df = pd.read_excel("화장품_매출액.xlsx")

df.columns = ['area', 'service', 'sales'] # 열 제목을 영문으로 바꿀 때 사용

# load data file
sns.boxplot(x='area', y='sales', hue='service', data=df)
plt.show()

# 교호작용 그래프
from statsmodels.graphics.factorplots import interaction_plot
fig = interaction_plot(df.area, df.service, df.sales)
plt.show()

model = ols('sales ~ C(area) + C(service) + C(area):C(service)', data=df).fit()
print(model)
print(anova_lm(model))
# p-adj 값이 0.05보다 크므로, reject 할 수 없다(false) -> 유의미한 차이가 없다
tukey = pairwise_tukeyhsd(df['sales'], df['area'], alpha=0.05)
print(tukey)
print()
tukey = pairwise_tukeyhsd(df['sales'], df['service'], alpha=0.05)
print(tukey)