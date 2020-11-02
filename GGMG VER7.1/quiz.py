import pandas as pd
import numpy as np
import csv
import matplotlib as plt
import random

with open('animal.csv', 'w', encoding='UTF-8') as writer_csv:
    name_list = ['Question', 'Answer', 'Explanation']
    writer = csv.DictWriter(writer_csv, fieldnames=name_list)
    writer.writeheader()
    writer.writerow({'Question': '북극곰은 겨울잠을 잔다', 'Answer': 'X',
                     'Explanation': '동물이 겨울에 잠을 자는 이유는 먹이가 없기 때문. 북극곰은 겨울잠을 자지 않는다'})
    writer.writerow({'Question': '하마는 말의 일종이다', 'Answer': 'X',
                     'Explanation': '하마는 돼지의 일종이다'})
    writer.writerow({'Question': '물고기는 기침을 한다', 'Answer': 'O',
                     'Explanation': '물고기는 물이 오염될 수록 기침을 한다'})
    writer.writerow({'Question': '두꺼비는 이가 없다', 'Answer': 'O',
                     'Explanation': '두꺼비는 이가 아예 없다'})
    writer.writerow({'Question': '철새는 이동 중에 잠을 잔다', 'Answer': 'O',
                     'Explanation': '뇌의 절반씩 교대로 잠을 자는 가수면 상태에서 비행한다'})

with open('plant.csv', 'w', encoding='UTF-8') as writer_csv:
    name_list = ['Question', 'Answer', 'Explanation']
    writer = csv.DictWriter(writer_csv, fieldnames=name_list)
    writer.writeheader()
    writer.writerow({'Question': '버섯은 식물이다', 'Answer': 'X',
                     'Explanation': '버섯은 균류에 속한다'})
    writer.writerow({'Question': '어성초는 비린 향이 난다', 'Answer': 'O',
                     'Explanation': '어성초에서는 비린 향이 난다'})
    writer.writerow({'Question': '인삼은 꿀에 재 놓아야 좋다', 'Answer': 'X',
                     'Explanation': '꿀에 재 놓으면 일종의 독소성분이 발생하므로 좋지 않다'})
    writer.writerow({'Question': '이끼는 건조하거나 햇빛이 잘 비치는 곳에서 잘 자란다',
                     'Answer': 'X', 'Explanation': '이끼는 그늘지고 습기가 많은 곳에서 잘 자란다'})
    writer.writerow({'Question': '동충하초는 식물이다', 'Answer': 'X',
                     'Explanation': '곤충류나 거미류에 기생하며 숙주가 죽은 후에 그 체표에 다양한 형상, 크기, 색상을 가진 자실체를 형성하는 곤충기생성 자낭균류이다'})

with open('health.csv', 'w', encoding='UTF-8') as writer_csv:
    name_list = ['Question', 'Answer', 'Explanation']
    writer = csv.DictWriter(writer_csv, fieldnames=name_list)
    writer.writeheader()
    writer.writerow({'Question': '예방 접종은 병을 치료하기 위해서 하는 것이다',
                     'Answer': 'X', 'Explanation': '예방접종은 병에 걸리지 않기 위하여 하는 것입니다'})
    writer.writerow({'Question': '사람들이 병에 걸리는 것은 반드시 균 때문이다',
                     'Answer': 'X', 'Explanation': '병의 원인은 균뿐만이 아닙니다'})
    writer.writerow({'Question': '감기 균은 공기를 통해서 전염된다', 'Answer': '',
                     'Explanation': '감기 균은 공기 중에 퍼져 다니다가 호흡기를 통해 감염됩니다'})
    writer.writerow({'Question': '음식을 아무리 잘 씻어도 병균을 완전히 씻어내는지는 못한다',
                     'Answer': 'O', 'Explanation': '세제나 물로 아무리 깨끗하게 씻어도 균을 완전히 씻어내지는 못합니다'})
    writer.writerow({'Question': '음식물로 들어온 균은 대부분 위 속에서 죽는다', 'Answer': 'O',
                     'Explanation': '위 속에는 아주 강한 산이 있어서 병균이 들어오면 견디지 못하고 죽습니다'})

df_a = pd.read_csv('animal.csv')
df_h = pd.read_csv('health.csv')
df_p = pd.read_csv('plant.csv')

frames = [df_a, df_h, df_p]
df_rand = pd.concat(frames, ignore_index=True)

animal = df_a.values.tolist()
health = df_h.values.tolist()
plant = df_p.values.tolist()
all = df_rand.values.tolist()


# animal quiz 시작
np.random.seed(1)
my_score = 0

index_a = random.randint(0, len(animal)-1)
animal[index_a][0]

user_ans = input()
animal[index_a][1:3]

if user_ans == animal[index_a][1]:
    print('정답')
    my_score += 1
else:
    print('오답')

my_score


def Animal():
    np.random.seed(8)
    my_score = 0
    for i in range(5):

        index_a = random.randint(0, len(animal)-1)
        print('문제 : ', animal[index_a][0])
        user_ans = input()
        print('해설 : ', animal[index_a][1:3])

        if user_ans == animal[index_a][1]:
            print('정답')
            my_score += 1
            #print('점수 : +', my_score)
        else:
            print('오답')
            #print('점수 :', my_score)
        a = my_score
        print(a)

    print('총점 :', a)


Animal()
