import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (12, 6)

df = pd.read_csv('Census_2016_2021.csv', index_col=0, delimiter=',', decimal='.', encoding="utf-8")
df = df[df['Type'] == 'MÉ']
df['Pop moyenne'] = (df["Pop21"] + df["Pop16"]) / 2
print('Le nombre de municipalité est de ', df.shape[0], ".")
print("La population moyenne pour chaque ville est :\n", df[["Nom", 'Pop moyenne']])
df['PctAcc'] = 100 * (df['Pop21'] - df['Pop16']) / df['Pop16']

df.plot(kind='scatter', x='Pop21', y='PctAcc')
plt.ylabel('Accroissement de la population de 2016 a 2021 [%]')
plt.xlabel("Population en 2021")
plt.show()

bins = [0, 2000, 10000, 25000, 100000, np.inf]
print(bins)
df['Classement'] = pd.cut(df['Pop21'], bins, labels=['moins de 2000', '2000 à 9999', '10000 à 24999',
                                                     '25000 à 99999', '100000 et plus'])

occurrences_labels = df['Classement'].value_counts()
print(occurrences_labels)
occurrences_labels.plot(kind='barh', x='Nombre de ville', y='Tranche de population')
plt.xlabel('Nombre de ville')
plt.ylabel('Tranche de population')
plt.show()
