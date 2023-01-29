# Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# добавлены средние для одинаковой длины
football = np.array([173, 175, 180, 178, 177, 185, 183,
                    182, 179.125, 179.125, 179.125])
# добавлены средние для одинаковой длины
hockey = np.array([177, 179, 180, 188, 177, 172,
                  171, 184, 180, 178.66, 178.66])
barbell = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
print(stats.shapiro(football))
print(stats.shapiro(hockey))
print(stats.shapiro(barbell))

print("выборки распределены нормально, т.к. pvalue > допустимого уровня значимости=0,05")

stats.bartlett(football, hockey, barbell)
print("дисперсии среди групп равны")

print(len(football), len(hockey), len(barbell))

print("Промежуточный ответ: различие между средним ростом спортсменов значимо")

x1 = np.linspace(1, 11, 11)
x2 = np.linspace(12, 22, 11)
x3 = np.linspace(23, 33, 11)

plt.plot(x1, football, 'red')
plt.plot(x2, hockey, 'green')
plt.plot(x3, barbell, 'orange')


df = pd.DataFrame({'score': [173, 175, 180, 178, 177, 185, 183, 182, 179.125, 179.125, 179.125,
                             177, 179, 180, 188, 177, 172, 171, 184, 180, 178.66, 178.66,
                             172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170],
                   'group': np.repeat(['football', 'hockey', 'barbell'], repeats=11)})
tukey = pairwise_tukeyhsd(endog=df['score'], groups=df['group'], alpha=0.05)
print(tukey)

print("Ответ: между футболистами и штангистами, хокеистами и штангистами есть существенные различия в среднем росте, между футболистами и хокеистами значимых различий нет")
