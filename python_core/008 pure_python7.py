#dictionary
#딕셔너리는 {} 를 사용, 데이터가 짝(pair)로 다님


#메뉴판 만들기
menu_price = {
    "아메리카노": 1500,
    "라떼": 2500,
    "에스프레소": 2000
}
#리스트는 번호로 값을 꺼내고, 딕셔너리는 이름으로 꺼냄
print(menu_price["아메리카노"])

print(f"라떼는 {menu_price['라떼']}원 입니다.")

#있는지 물어보는 것
order = "카푸치노"
if order in menu_price:
    print("네, 있습니다.")
else:
    print("죄송하지만 없는 메뉴입니다.")



#스마트 키오스크
#시작
print("=== 스마트 키오스크 ===")
#메뉴 및 가격 설정
menu_price = {
    "에스프레소": 1000,
    "아메리카노": 1500,
    "카페라떼": 2000
}
#메뉴판 보여주기
print("\n--- 메뉴판 ---")
for key in menu_price:
    print(f"{key} : {menu_price[key]}원")
print("------------\n")

total_price = 0

while True:
    order = input("메뉴를 골라주세요.(종료는 q): ").strip() #실수로 들어간 공백 제거하는 것 .strip()

    if order == 'q':
        print(f"주문을 종료합니다. 총 금액은 {total_price}원 입니다.")
        break

    elif order in menu_price:
        total_price += menu_price[order]
        print(f">{order} 추가됨. (누적: {total_price}원)")

    else:
        print(f"{order}는 없는 메뉴입니다. 다시 확인해주세요.")


#다음시간 함수 복습!