
from __future__ import division
from scipy.io import loadmat
import pandas as pd
from PIL import Image
import os.path

# annots = loadmat('car_devkit/cars_test_annos.mat')
annots = loadmat('/content/car_dataset/cars_annos.mat')

data = [[row.flat[0] for row in line] for line in annots['annotations'][0]]

# columns = ['fname', 'bbox_x1 [Min X]', 'bbox_y1 [Min Y]', 'bbox_x2 [Max X]', 'bbox_y2 [Max Y]', 'class', 'Is Test']
columns = ['fname', 'bbox_x1', 'bbox_y1', 'bbox_x2', 'bbox_y2', 'class', 'Is Test']

df_train = pd.DataFrame(data, columns=columns)

# df_train.to_csv('text.csv', sep='\t', encoding='utf-8')

for index, row in df_train.iterrows():
    if os.path.isfile(row['fname']):
        im = Image.open(row['fname'])
        w, h = im.size
        a_w = row['bbox_x2'] - row['bbox_x1']
        a_h = row['bbox_y2'] - row['bbox_y1']
        a_x = (row['bbox_x2'] + row['bbox_x1'])/2
        a_y = (row['bbox_y2'] + row['bbox_y1'])/2
        file = open(row['fname'][:-4] + '.txt', "w")
        file.write(str(row['class']) + ' ' + str(a_x/w) + ' ' + str(a_y/h)+ ' ' + str(a_w/w) + ' ' + str(a_h/h))
        file.close()

# print(df_train.head())
