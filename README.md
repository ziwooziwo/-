# project1
``` python
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
f = open(r"C:\Users\A15\Downloads\범죄자_직업_2019.csv",encoding='euc-kr')
data = csv.reader(f)
font_path = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family = font)

results = np.array([[3,0,12,2,2,28,1,1,0,58,1,3,12,66,54,1,0,2,5,0,5,13,4,0,16,13,0,1,395,244],
                    [75,72,280,84,103,727,166,105,8,5525,39,90,288,904,1982,149,14,54,118,23,124,869,420,4,4633,49,14,83,6961,5249],
                    [2,1,9,2,12,25,6,6,0,228,1,18,15,84,136,44,0,3,7,1,48,82,2,4,143,89,1,6,1150,614]])

crime = ['살인','성폭행','마약']
job = []

for i in data:
    if '범죄분류' in i[0]:
        for x in i[1:]:
            job.append(x)
        print(job)

fig, ax = plt.subplots()
im = ax.imshow(results)

ax.set_xticks(np.arange(len(job)))
ax.set_xticklabels(job)

ax.set_yticks(np.arange(len(crime)))
ax.set_yticklabels(crime)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(crime)):
    for j in range(len(job)):
        text = ax.text(j, i, results[i, j],
                       ha="center", va="center", color="w")

ax.set_title("범죄자 직업")
fig.tight_layout()
plt.show()


```
