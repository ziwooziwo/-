import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
f = open(r"C:\Users\A15\Downloads\범죄자_전과_2019.csv",encoding='euc-kr')
data = csv.reader(f)
font_path = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family = font)

results = np.array([[223,106,52,48,43,24,22,21,11,145,355],[11810,3750,2352,1603,1172,885,683,544,438,2658,7656],[1558,408,210,132,86,79,52,27,35,242,628]])

crime = ['살인','성폭행','마약']
num = []

for i in data:
    if '범죄분류' in i[0]:
        for x in i[1:]:
            num.append(x)
        print(num)

fig, ax = plt.subplots()
im = ax.imshow(results)

ax.set_xticks(np.arange(len(num)))
ax.set_xticklabels(num)

ax.set_yticks(np.arange(len(crime)))
ax.set_yticklabels(crime)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(crime)):
    for j in range(len(num)):
        text = ax.text(j, i, results[i, j],
                       ha="center", va="center", color="w")

ax.set_title("범죄에따른재범율")
fig.tight_layout()
plt.show()