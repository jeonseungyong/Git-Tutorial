#연습문제 3
def get_circle_area(radius):
  area=3.14*radius*radius
  return area
res1=get_circle_area(1)
res10=get_circle_area(10)
print(res1)
print(res10)

#연습문제 5
def get_radius(prompt):
  r=int(input(prompt))
  return r
res=get_radius('')**2*3.14
print(res)
