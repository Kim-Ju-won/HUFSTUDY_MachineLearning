import numpy as np
from math import sqrt


def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    result = user_1 - user_2
    result = result **2
    ans = sqrt(np.sum(result))
    return ans
    # 코드를 쓰세요 
    

# 실행 코드
user_1 = np.array([0, 1, 2, 3, 4, 5])
user_2 = np.array([0, 1, 4, 6, 1, 4])

distance(user_1, user_2)

