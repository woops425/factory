import pandas as pd
from scipy.stats import chisquare # 적합도 검정
from scipy.stats import  chi2_contingency # 독립성, 동질성 검정 모두에 사용

# 예제 6-11 : 주사위에 대한 '적합도' 검정
# obs_freq = [22, 19, 26, 25, 17, 11]
# exp_freq = [20, 20, 20, 20, 20, 20]
#
# from scipy.stats import chisquare
# result = chisquare(obs_freq, f_exp=exp_freq)
# print(result)

# 예제 6-12 : 남녀 간 만족도 차이에 대한 '독립성' 검정 - 행과 열이 서로 독립적인가?
# 식당의 만족도가 성별에 따라 차이가 있는지에 대해 가설을 세우고 유의수준 5% 하에서 검정하시오.
# 엑셀로 데이터 입력하는 거 상관 없음
# obs = pd.DataFrame({'남': [26,20,11], '여': [10, 15, 18]})
# obs.index=['만족', '보통', '불만족']
# print(obs)
# from scipy.stats import  chi2_contingency
# result = chi2_contingency(obs, correction = False)
# print(result)

# 예제 6-13 : 찬반 의견에 대한 동질성 검정 - 열의) 비율이 같은가?
obs = pd.DataFrame({'남': [25, 75], '여': [45, 55]})
obs.index=['찬성', '반대']
print(obs)
from scipy.stats import  chi2_contingency
result = chi2_contingency(obs, correction = False)
print(result)