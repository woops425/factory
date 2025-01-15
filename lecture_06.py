from scipy.stats import norm

# mu = 0
# sigma = 1
#
# y1 = norm.cdf(0.5, mu, sigma)
# y2 = norm.cdf(-1.5, mu, sigma)
#
# print(y1)
# print(y2)
# print(y1 - y2)
# print()
# print("P(-1.5 <= Z <= 0.5) = ", y1 - y2)



mu = 0
sigma = 1
point = norm.ppf(0.9, mu, sigma)
point2 = norm.ppf(0.6915, mu, sigma)
print(point)
print(point2)