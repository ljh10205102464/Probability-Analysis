import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

prob = [0.825, 0.1, 0.05, 0.013, 0.007, 0.005]
back = [0.0888, 0.188, 0.288, 0.666, 0.888, 1]
prob = np.array(prob)
back = np.array(back)
get_once = 1430 * prob * back
print('一次返还的期望:', get_once.sum())
fig=plt.figure()
plt.plot(prob,back,marker='o',linestyle='None')
plt.vlines(prob, 0, back)
plt.xlabel('一次返还概率')
plt.ylabel('一次返还比例')
plt.title('王者点券返还活动一次返还概率分析')

get_quad = []
# C_6^1 6
prob_C_61 = []
back_C_61 = []
back_C_61_copy = []
for i in range(6):
    prob_C_61.append(pow(prob[i], 4))
    tmp = (4 * back[i]) / 4
    back_C_61.append(1430 * prob_C_61[-1] * tmp)
    back_C_61_copy.append(tmp)

# C_6^2 30
prob_C_62 = []
back_C_62 = []
back_C_62_copy = []
for i in range(6):
    for j in range(i + 1, 6):
        prob_C_62.append(4 * pow(prob[i], 3) * prob[j])
        tmp = (3 * back[i] + back[j]) / 4
        back_C_62.append(1430 * prob_C_62[-1] * tmp)
        back_C_62_copy.append(tmp)

# C_6^3 150
prob_C_63 = []
back_C_63 = []
back_C_63_copy = []
for i in range(6):
    for j in range(i + 1, 6):
        for m in range(j, 6):
            if (j == m):
                prob_C_63.append(6 * pow(prob[i], 2) * pow(prob[j], 2))
                tmp = (2 * back[i] + 2 * back[j]) / 4
                back_C_63.append(1430 * prob_C_63[-1] * tmp)
                back_C_63_copy.append(tmp)
            else:
                prob_C_63.append(12 * pow(prob[i], 2) * prob[j] * prob[m])
                tmp = (2 * back[i] + back[j] + back[m]) / 4
                back_C_63.append(1430 * prob_C_63[-1] * tmp)
                back_C_63_copy.append(tmp)

# C_6^4 360
prob_C_64 = []
back_C_64 = []
back_C_64_copy = []
for i in range(6):
    for j in range(i + 1, 6):
        for m in range(j + 1, 6):
            for n in range(m + 1, 6):
                prob_C_64.append(24 * prob[i] * prob[j] * prob[m] * prob[n])
                tmp = (back[i] + back[j] + back[m] + back[n]) / 4
                back_C_64.append(1430 * prob_C_64[-1] * tmp)
                back_C_64_copy.append(tmp)

back_C_61 = np.array(back_C_61)
back_C_62 = np.array(back_C_62)
back_C_63 = np.array(back_C_63)
back_C_64 = np.array(back_C_64)
prob_C_61 = np.array(prob_C_61)
prob_C_62 = np.array(prob_C_62)
prob_C_63 = np.array(prob_C_63)
prob_C_64 = np.array(prob_C_64)
print('四次返还的概率和:', prob_C_61.sum() + prob_C_62.sum() + prob_C_63.sum() + prob_C_64.sum())
print('四次返还的期望:', back_C_61.sum() + back_C_62.sum() + back_C_63.sum() + back_C_64.sum())

X = np.hstack((prob_C_61, prob_C_62, prob_C_63, prob_C_64))
Y = np.hstack((back_C_61_copy, back_C_62_copy, back_C_63_copy, back_C_64_copy))
fig=plt.figure()
plt.plot(X,Y,marker='o',linestyle='None')
plt.vlines(X, 0, Y)
plt.xlabel('四次返还概率')
plt.ylabel('四次返还比例')
plt.title('王者点券返还活动四次返还概率分析')
plt.show()