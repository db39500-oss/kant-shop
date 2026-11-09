items = []

class Shop:
    # 게임 타이틀 보이기
    def show_title(self):
        print("-"* 55)
        print(f"1. 상품목록 2. 담기 3. 빼기 4. 장바구니 5. 쿠폰 6. 결제 q. 종료")
        print("-"* 55)

    # 1. 상품 목록 보이기
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = int(price)
        self.inventory = int(inventory)
        
        items.append(self)

    # 장바구니 목록 보이기
    def show_basket(self):
            
        for num, item in enumerate(items, start=1):
            if item.inventory != 0:
                print(f" {num}. {item.name}    {item.price:,}원   (재고 {item.inventory}개)")
            else:
                print(f" {num}. {item.name}    {item.price:,}원   (품절)")

        
            # if self.inventory == 0:
            #     item.inventory = "품절"
        

shop1 = Shop("무선 이어폰", 89000, 3)
shop2 = Shop("텀블러", 15000, 10)
shop3 = Shop("보조배터리", 32000, 5)
shop4 = Shop("마우스패드", 9000, 0)
shop5 = Shop("USB 허브", 18000, 4)


shop1.show_title()
shop1.show_basket()