#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##연도별 지점 먼지 평균
df_PMyear=df_PM.copy()
df_PMyear['TM']=pd.to_datetime(df_PMyear['TM'])
df_PMyear=df_PMyear.groupby([df_PMyear['TM'].dt.year,'STN_KO','STN_ID']).mean(numeric_only=True).reset_index()
df_PMyear['TM']=df_PMyear['TM'].astype('str')

df_PMyear_nm=df_PMyear['STN_KO'].unique()

## 시각화
plt.figure(figsize=(10, 6))
for i in df_PMyear_nm:
    plt.plot(df_PMyear[df_PMyear['STN_KO']==i]['TM'],df_PMyear[df_PMyear['STN_KO']==i]['PM10'],label=i)

plt.title('연도별 PM10농도',pad=15,size=20)
plt.xlabel('년도',loc='right',labelpad=10,fontsize=15)
plt.ylabel('PM10(µg/m³)',loc='top',labelpad=10,fontsize=15)

plt.xlim(df_PMyear['TM'].min(), df_PMyear['TM'].max())

xticks_lable = ['2014년','2015년','2016년','2017년','2018년','2019년','2020년','2021년','2022년','2023년']
plt.xticks(range(0,10,1),labels=xticks_lable)
plt.legend(loc=(1,0))

plt.show()

