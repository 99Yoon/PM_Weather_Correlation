#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## 주요 도시 미세먼지 80> 비율

def up80(x):
    if x>80:
        return 1
    else:
        return 0
df_PM_copy['80>']=df_PM_copy['PM10'].apply(up80)
df_PM_copy=df_PM_copy[df_PM_copy['STN_ID'].isin(loc_lst)]

df_PM_copy_per=df_PM_copy.groupby(['STN_KO']).agg({'80>': 'sum','STN_KO': 'size'})

df_PM_copy_per['per']=df_PM_copy_per['80>']/df_PM_copy_per['STN_KO']

df_PM_copy_idx=['광주(전남)','대구(경북)','서울','속초(강원)','수원(경기)','울릉도(경북)','울산(경남)','울진(경북)','전주(전북)','춘천(강원)']
df_PM_copy_per.index=df_PM_copy_idx

plt.figure(figsize=(10,6), facecolor='ivory', edgecolor='k', linewidth=2)
plt.pie(df_PM_copy_per['per'], labels=df_PM_copy_per.index, labeldistance = 1.2,autopct ='%.1f%%',
       wedgeprops = {'lw':1 ,'width':0.8})
plt.legend(loc=(1.3,0.5))
plt.title('주요 도시 미세먼지 나쁨 비율',size=15)
plt.show()

