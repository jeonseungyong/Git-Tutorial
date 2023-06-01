Python 3.12.0a5 (tags/v3.12.0a5:3c67ec3, Feb  7 2023, 16:36:51) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pickle
import os

filepath='score.bin'
class Score:
    def __init__(self):
        self.scores = []

    def input_scores(self):
      i=1
      while True:      
        n=int(input(f'#{i}?'))
...         if n<0:
...           break
...         self.scores.append(n)
...         i+=1
...             
...     def get_average(self):
...         total = sum(self.scores)
...         return total / len(self.scores)
... 
...     def show_scores(self):
...         for n in self.scores:
...             print(n, end=' ')
...         print()
... 
...     def save_scores(self, filepath):
...         with open(filepath, 'wb') as file:
...             pickle.dump(self.scores, file)
... 
...     def load_scores(self, filepath):
...         with open(filepath, 'rb') as file:
...             self.scores = pickle.load(file)
... 
... if os.path.exists(filepath):
...   print('[파일읽기]')
...   print('[점수출력]')
...   s.load_scores(filepath)
...   print('개인점수: ',end='')
...   s.show_scores()
...   print('평균: ',end='')
...   print(s.get_average())
... else:
...   s=Score()
...   print('[점수 입력]')
...   s.input_scores()
...   print('[점수 출력]')
...   print('개인점수: ',end='')
...   s.show_scores()
...   print('평균: ',end='')
...   print(s.get_average())
