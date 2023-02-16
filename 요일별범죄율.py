import csv
f = open("C:\\Users\\a13\\Desktop\\web\\day33\\범죄발생_요일_2019.csv",encoding='euc-kr')
data = csv.reader(f)
sal = []
sung = []
ma = []
day = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
for i in data:
    if '살인' in i[0]:
        for x in i[1:]:
            sal.append(int(x))
    if '성폭력' in i[0]:
        for j in i[1:]:
            sung.append(int(j))
    if '마약' in i[0]:
        for z in i[1:]:
            ma.append(int(z))
#         print(sal)
#         print(sung)
#         print(ma)
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family = font)
plt.xlabel('Day')
plt.ylabel('Count')
plt.title('요일별 범죄 건수')
plt.plot(sal, label = '살인', color = 'red')
plt.plot(sung, label = '성폭력', color = 'orange')
plt.plot(ma, label = '마약', color = 'blue')
plt.legend()
plt.show()