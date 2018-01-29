number = 0
prompt = """선택하세요
1. 더하기
2. 뺴기
3. 나누기
4.종료
당신의 번호는? """

while True:
    print(prompt)
    number = int(input())
    if number == 4:
        break