# 누적계산 (accumulation)

def get_item_price(price, tax=1.1):
    return int(price * tax)

cart_prices = [1000, 2000, 1500, 3000]

total_sum = 0

print("=== 계산 시작 ===")
for price in cart_prices:
    final_price = get_item_price(price)
    total_sum = total_sum + final_price
    print(f"물건 추가됨: {final_price}원 (현재 합계: {total_sum}원)")

print("=== 계산 종료 ===")
print("최종 결제 금액:", total_sum)





# input

print("=== 타일 면적 계산기 ===")
width = input("가로 길이를 입력하세요(m): ")
width = int(width)
area = width * width
print(f"정사각형 타일의 면적은 {area} 제곱미터입니다.")




print("=== 환율 계산기 ===")
dollar = input("달러 금액을 입력하세요: ")
dollar = int(dollar)
currency = dollar * 1400
print(f"원화로 {currency}원입니다.")


# 더 간단하게 쓰는 방법
dollar = input("달러 금액을 입력하세요: ")
dollar = int(dollar)
# 아래와 같이 줄여서 쓸 수 있음
dollar = int(input("달러 금액을 입력하세요: "))
