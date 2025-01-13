import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import binom
from scipy.stats import norm

# # 이항확률분포의 확률계산 - 5주차 26p
# n = 5
# p = 0.5

# # 0~n까지의 리스트 생성(확률변수)
# x = np.arange(n+1)
# mean, var = binom.stats(n, p)
#
# # list x의 각 확률변수 r에 대한 확률을 list로 생성하여 prob에 저장
# prob = binom.pmf(x, n, p)
# print("mean = ", mean, "var = ", var)
#
# plt.bar(x, prob)
# plt.xlabel("X")
# plt.ylabel("P(X)")
# plt.title("binomial distribution(n = 5, p = 0.5)")
# plt.show()
# print(prob)


# 평균이 50이고 표준편차가 5인 정규분포 그래프 작성 - 34p
mu = 50
scale = 5

x = np.arange(mu-30, mu+30, 0.1)
y = norm.pdf(x, mu, scale)

plt.bar(x,y)
plt.xlabel("X")
plt.ylabel("f(X)")
plt.title("normal distribution(mu = 50, sigma = 5)")
plt.show()