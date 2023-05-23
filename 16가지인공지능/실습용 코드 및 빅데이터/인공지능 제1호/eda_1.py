import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./data/학생건강검사 결과분석 rawdata_서울_2015.csv')
df.head()