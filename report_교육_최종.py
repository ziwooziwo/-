import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import font_manager, rc
font_path = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family = font)
with open(r"C:\Users\a13\Desktop\web\day33\범죄자_교육정도_2019.csv",encoding="cp949") as f:
    data = csv.reader(f)
    a = []
    sort_edu = []
    for i in data:
        # print(i)
        a.append(i)
    for i in range(len(a[0])):
        sort_edu.append(a[0][i])
# i[1] i[16]부터
# print(type(data))
kill = a[1][:]
kill1 = []
assult = a[2][:]
assult1 = []
drug = a[4][:]
drug1 = []
sort_edu.remove("범죄분류")
assult.remove("성폭력")
kill.remove("살인")
drug.remove("마약류관리에관한법률(마약)")
for i in kill:
    kill1.append(int(i))
for i in assult:
    assult1.append(int(i))
for i in drug:
    drug1.append(int(i))
# print(drug)
# print(kill)
# print(drug)
# print(sort_edu)
# print(a)
print(type(kill))
# y = [a[1][0],a[2][0],a[5][0]]
# count = [kill]
x = np.arange(0,19,1)
# print(count)
# print(len(kill))
# print(sort_edu)
fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
fig.subplots_adjust(hspace=0.05)
# ax1.plot(x,kill1,label="살인")
ax1.plot(x,assult1,c ="red", label="성폭행")
# ax1.plot(x,drug1, label="마약")

ax2.plot(x,kill1,label="살인")
# ax2.plot(x,assult1,label="성폭행")
ax2.plot(x,drug1, label="마약")

# ax1.set_ylim(700, 10000)
# ax2.set_ylim(0, 500)

# ax1.spines["bottom"].set_visible(False)
# ax2.spines["top"].set_visible(False)
# ax1.xaxis.tick_top()
# ax1.tick_params(labeltop=False)
# ax2.xaxis.tick_bottom()

# kwargs = dict(marker=[(-1, -0.5), (1, 0.5)], markersize=12,
#               linestyle="none", color='k', mec='k', mew=1, clip_on=False)
# ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
# ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# ax1.xticks(x, sort_edu, rotation=45)

# plt.plot(x,kill1,label="살인")
# plt.plot(x,assult1,label="성폭행")
# plt.plot(x,drug1, label="마약")
plt.xticks(x, sort_edu, rotation=90)
ax1.set(title='범죄자의 교육정도')
ax1.legend()
plt.legend()
plt.show()