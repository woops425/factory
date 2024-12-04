import math
from scipy.stats import norm

# 주어진 값
mu_0 = 120  # 가정된 평균
sample_mean = 122  # 표본 평균
sigma = 15  # 표본 표준편차
n = 25  # 표본 크기
alpha = 0.05  # 유의수준

# 우측 단측검정(greater) : 검정통계량 z가 임계값보다 크면 H0 기각
# 좌측 단측검정(less) : 검정통계량 z가 임계값보다 작으면 H0 기각

# 임계값 계산 (단측 검정) - 유의수준 하에서의
z_critical = norm.ppf(1 - alpha)

# 검정 통계량 계산
z = (sample_mean - mu_0) / (sigma / math.sqrt(n))

print("검정 통계량 : " ,z)
print("유의수준 ", alpha*100, "%에서의 임계값 : ", z_critical)
