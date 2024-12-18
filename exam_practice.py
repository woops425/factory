import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
import scipy.stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import seaborn as sns


# 기출
# 4번 문제
# 데이터 입력

obj = [65, 78, 66, 54, 84, 74, 55]
short = [69, 79, 56, 53, 86, 74, 45]
essay = [56, 67, 76, 86, 75, 65, 58]

# ANOVA 분석
f_stat, p_value = scipy.stats.f_oneway(obj, short, essay)

# 결과 출력
print("F-statistic:", f_stat)
print("p-value:", p_value)
print()
df = pd.DataFrame({'product': obj+short+essay, 'group':np.repeat(['obj', 'short', 'essay'], repeats=7)})
print(df)
print()
print(f_oneway(obj,short,essay))
# p-value 값이 0.05보다 큼 -> H0 채택 : 그룹 간 차이가 유의미하지 않다.
result = pairwise_tukeyhsd(df['product'],df['group'],alpha=0.05)
print(result)

print(scipy.stats.f_oneway(obj,short,essay))
