
from __future__ import division
from scipy.io import loadmat
import pandas as pd
from PIL import Image
import os.path

annots = loadmat('cars_meta.mat')
data = [[row.flat[0] for row in line] for line in annots['class_names'][0]]

columns = ['class']
df_train = pd.DataFrame(data, columns=columns)

file = open('class_names.txt', "w")
for index, row in df_train.iterrows():
    file.write(str(row['class']) + '\n')
file.close()
# print(df_train.head())
