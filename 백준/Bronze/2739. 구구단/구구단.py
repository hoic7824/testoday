# 1. 안내 문구 없이 입력만 받습니다.
N = int(input())

# 2. 1부터 9까지 반복합니다.
for num in range(1, 10):
    # 3. 문제에서 요구한 "N * num = 결과" 형식만 출력합니다.
    print(f"{N} * {num} = {N * num}")