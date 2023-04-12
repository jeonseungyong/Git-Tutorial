def read_single_digit(num):
  if num==0:
    return '영'
  elif num==1:
    return '일'
  elif num==2:
    return '이'
  elif num==3:
   return '삼'
  elif num==4:
    return '사'
  elif num==5:
    return '오'
  elif num==6:
    return '육'
  elif num==7:
    return '칠'
  elif num==8:
    return '팔'
  elif num==9:
    return '구'

def read_number(num):
  if 10<=num<100:
    num10=num//10
    num%=10
    return read_single_digit(num10)+read_single_digit(num)
  elif 100<=num<1000:
    num100=num//100
    num%=100
    num10=num//10
    num%=10
    return read_single_digit(num100)+read_single_digit(num10)+read_single_digit(num)
    

num=int(input('세 자리 정수 입력: '))
if num<10:
  print(read_single_digit(num))
elif 10<=num<1000:
   print(read_number(num))
