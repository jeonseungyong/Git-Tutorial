shopping_bag =[]
amount={'사과':'10','바나나':'2'}
print('[구입]')
while True:
  item = input('상품명?')
  if item=='':
    break
  shopping_bag.append(item)
  print('수량은?',amount.get(item))
  print(f'장바구니에 {item}',end='')
  print(amount.get(item),end='')
  print(f'개가 담겼습니다.')
print(f'\n>>> 장바구니 보기: {amount}')  

print('[검색]')
item=input('장바구니에서 확인하고자 하는 상품은?')
print(f'{item}은(는)',end='')
print(amount.get(item),end='')
print(f'개 담겨있습니다.')
