import pandas as pd

# 구분자 설정 (예: 탭 구분자)
data = pd.read_csv("data/korean/nsmc/ratings_train.txt", sep='\t', header=None)

# 데이터 출력
print(data.head())
