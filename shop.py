stocks = [] # 상품 재고
my_items = [] # 장바구니 리스트

class Shop:
    # 게임 타이틀 보이기
    def show_title(self):
        print("-"* 55)
        print(f"1. 상품목록 2. 담기 3. 빼기 4. 장바구니 5. 쿠폰 6. 결제 q. 종료")
        print("-"* 55)

    def intro(self):
        while True:
            number = input("\n메뉴 선택 번호를 입력해주세요. : ")

            if number == "1":
                self.show_basket()
            
                
            elif number == "2":
                product_num = int(input("상품 번호: "))
                qty = int(input("수량: "))
                
                self._add_basket(product_num, qty)

            elif number == "3":
                product_num = int(input("장바구니에서 뺄 상품을 입력해주세요. : "))
                qty = int(input("뺄 수량: "))

                self._take_out_basket(product_num, qty)
                
            elif number == "4":
                self.show_my_basket()
                
            # elif number == "5":
            #     self.()
            #     break
            elif number == "q" or number == "Q":
                print("프로그램을 종료합니다.")
                break
            
            else:
                print("1 ~ 6 사이 값만 입력해주세요. 종료 원할 시 q 입력")
                

    # 상품 목록
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = int(price)
        self.inventory = int(inventory)

    # 상품 목록 보이기
    def show_basket(self):
        for num, item in enumerate(stocks, start=1):
            if item.inventory != 0:
                print(f" {num}. {item.name}    {item.price:,}원   (재고 {item.inventory}개)")
            else:
                print(f" {num}. {item.name}    {item.price:,}원   (품절)")


    # 내 장바구니 보기
    def show_my_basket(self):
        print("\n" + "=" * 55)
        print("[내 장바구니 리스트]")
        for num, item in enumerate(my_items, start=1):
            print(f"{num}. {item.name}    {item.price:,}원   (수량 {item.inventory}개)")

    # 장바구니 뺴기
    def _take_out_basket(self, product_num, qty):
        if product_num < 1 or product_num > len(my_items):
            print("잘못된 상품 번호입니다.")
            return

        basket_item = my_items[product_num - 1]

        if qty <= 0:
            print("1개 이상 입력해주세요.")
            return

        if qty > basket_item.inventory:
            print(f"장바구니 수량이 부족합니다. (현재 수량: {basket_item.inventory}개)")
            return

        # 재고 복구
        for stock_item in stocks:
            if stock_item.name == my_items.name:
                stock_item.inventory += qty
                break

        # 장바구니 수량 차감
        basket_item.inventory -= qty

        # 수량이 0이면 장바구니에서 상품 삭제
        if basket_item.inventory == 0:
            my_items.remove(basket_item)

        print(f"{basket_item.name} {qty}개를 장바구니에서 뺐습니다.")
        

    # 장바구니 담기
    def _add_basket(self, product_num, qty):
        if product_num < 1 or product_num > len(stocks):
            print("잘못된 상품 번호입니다.")
            return

        item = stocks[product_num - 1]

        if item.inventory == 0:
            print("품절된 상품입니다.")
            return 

        if qty > item.inventory:
            print(f"재고가 부족합니다. (담을 수 있는 수량: {item.inventory}개)")
            return

        if qty <= 0:
            print("1개 이상의 수량을 입력해주세요.")
            return

        item.inventory -= qty

        for basket_item in my_items:
            if basket_item.name == item.name:
                basket_item.inventory += qty
                break
        else:
            my_items.append(Shop(item.name, item.price, qty))

        print(f"{item.name} {qty}개를 담았습니다.")


# 상품 목록 리스트 만들기
shop1 = Shop("무선 이어폰", 89000, 3)
shop2 = Shop("텀블러", 15000, 10)
shop3 = Shop("보조배터리", 32000, 5)
shop4 = Shop("마우스패드", 9000, 0)
shop5 = Shop("USB 허브", 18000, 4)

# stocks.append(shop1)
# stocks.append(shop2)
# stocks.append(shop3)
# stocks.append(shop4)
# stocks.append(shop5)
stocks.extend([shop1, shop2, shop3, shop4, shop5])


shop1.show_title()
shop1.intro()
