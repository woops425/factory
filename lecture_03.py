import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 히스토그램

data = pd.read_excel("중학생_남자_키.xlsx")
# print(data[0:5])
plt.hist(data, label='bins=14', bins=14) # 막대 수를 5로 하고 범례(label)의 내용 작성
plt.legend()    # 범례('bins=5')를 그래프에 배치함
# plt.xlabel("height")
# plt.title("Histogram")
plt.show() # 히스토그램을 화면에 출력

# plt.hist(data, label='bins=7', bins=7) # 막대 수를 7로 하고 레이블 작성
# plt.legend()
# plt.show()
#
# plt.hist(data, label='bins=10', bins=10) # 막대 수를 10으로 하고 레이블 작성
# plt.legend()
# plt.show()


# 막대 그래프

# x = [6,7,8,9,10,11] # x축에 나타낼 6개의 값(리스트 사용)
# y = [16109, 41401, 53121, 59899, 53450, 82565] # y축의 값
#
# plt.bar(x,y) # x축과 y축의 데이터
# # plt.title
# plt.show()

# 파이 차트
# ratio = [22,24,16,38] # 퍼센트 비율(전체 합은 100)
# labels = ['pizza', 'hamburger', 'pasta', 'chicken'] # 각 퍼센트의 레이블
# plt.pie(ratio, labels=labels, autopct='%.1f%%') # 퍼센트의 표시방법
# plt.show()

# 선 그래프(=꺾은선 그래프)
# x = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
# y1 = [14.4, 14.5, 15.4, 16.9, 17.8, 17.6, 27.6]
# y2 = [20.5, 21.0, 22.8, 23.6, 24.2, 24.3, 29.5]
#
# plt.plot(x,y1, linestyle='solid',color = 'red', label='teens')
# plt.plot(x,y2, linestyle='dashed',color = 'blue', label='20s')
# plt.legend(loc='best', ncols=1)
# plt.show()

# 상자 도형(box plot)
# data = pd.read_csv("스마트폰_이용시간.csv")
# print('median = ', np.median(data))
# print('min = ', np.min(data)) # 최솟값

# # y1 = [14.4, 14.5, 15.4, 16.9, 17.8, 17.6, 27.6]
#
# plt.boxplot(data, vert=True) # 세로로 나옴
# plt.show()


# 산점도(scatter plot)

# data = pd.DataFrame(pd.read_excel("초등학생_키몸무게.xlsx"))
# print(data[0:5])
# # print(data.height[0:5])
#
# plt.scatter(data.height, data.weight, c='red')
# plt.show()

# 아이리스 데이터에 대한 산점도 행렬 작성
# iris = sns.load_dataset('iris')
# iris.head()
#
# sns.pairplot(iris, diag_kind='hist')
# plt.show()

