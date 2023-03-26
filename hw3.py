def get_fixed_price(discount_rate, discount_price):
    original_price = discount_price / (1 - discount_rate / 100)
    return original_price

discount_rate=int(input("할인율은? "))
Adp=int(input("A 상품의 할인된 가격은? "))
Bdp=int(input("B 상품의 할인된 가격은? "))
print("A 상품의 정가는",int(get_fixed_price(discount_rate,Adp)),"원")
print("B 상품의 정가는",int(get_fixed_price(discount_rate,Bdp)),"원")
