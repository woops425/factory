import numpy as np
import pandas as pd
from scipy import stats

## 과제 1번(대응 표본)
# data = pd.read_excel("1_파이썬 프로그래밍 성적.xlsx")
# print(data.describe())
#
# result = stats.ttest_rel(data.midterm, data.final, alternative='less')
# print(result)


## 과제 2번(독립 표본)
data = pd.read_excel("2_배터리 지속시간.xlsx")
print(data.describe())
# 중국과 한국 데이터 간의 사례 수가 차이가 있으므로, 파일을 분리하여 불러와야함
d1 = pd.read_excel("2_배터리 지속시간_중국.xlsx")
d2 = pd.read_excel("2_배터리 지속시간_한국.xlsx")
result = stats.ttest_ind(d1.china, d2.korea, alternative='two-sided')
print(result)

## 과제 3번(독립 표본)
# data = pd.read_excel("3_생수생산량.xlsx")
# print(data.describe())
#
# d1 = pd.read_excel("3_생수생산량_대전.xlsx")
# d2 = pd.read_excel("3_생수생산량_대구.xlsx")
# result = stats.ttest_ind(d1.daejeon, d2.daegoo, alternative='two-sided')
# print(result)
#
#
# ## 과제 4번(단일 표본)
# data = pd.DataFrame(pd.read_excel("4_S기업 점심비용.xlsx"))
# mu = 6300
# print(data.describe())
#
# result = stats.ttest_1samp(data, mu, alternative='two-sided')
# print(result)