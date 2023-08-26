#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df_abalone = pd.read_csv('./abalone_dataset.csv')
# %%
df_abalone.info()
# %%
df_abalone.head()
#%%
df_abalone['type'].value_counts()
# %%
df_abalone['type'].value_counts().plot(kind='bar')
# %%
pd.crosstab(df_abalone["sex"], df_abalone["type"])
# %%
pd.crosstab(df_abalone["sex"], df_abalone["type"]).plot(kind='bar')
plt.title("frequencia de tipo por genero")
plt.xlabel("genero")
plt.ylabel("qtd")
# %%
import seaborn as sns
corr_matrix = df_abalone.corr()
sns.heatmap(corr_matrix,fmt='.2f', annot=True,cmap='YlGnBu')
# %%
