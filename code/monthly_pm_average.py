#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## 월별로 각 지점의 미세먼지 수치 평균 계산

df_PM_month=df_PM.copy()
df_PM_month['TM']=pd.to_datetime(df_PM_month['TM'])
df_PM_month['time'] = df_PM_month['TM'].dt.month.astype('str').
                        str.zfill(2)
df_PM_month=df_PM_month.groupby(['time','STN_ID','STN_KO']).
                        mean(numeric_only=True).reset_index()
    
monSTN_uni=df_PM_month['STN_KO'].unique()

## 시각화

plt.figure(figsize=(10, 6))
for i in monSTN_uni:
    plt.plot(df_PM_month[df_PM_month['STN_KO']==i]['time'],
             df_PM_month[df_PM_month['STN_KO']==i]['PM10'],label=i)

plt.title('월별 PM10농도',pad=15,size=20)
plt.xlabel('월',loc='right',labelpad=10,fontsize=15)
plt.ylabel('PM10(µg/m³)',loc='top',labelpad=10,fontsize=15)

plt.xlim(df_PM_month['time'].min(), df_PM_month['time'].max())

xticks_lable = ['1월','2월','3월','4월','5월','6월','7월'
                ,'8월','9월','10월','11월','12월']
plt.xticks(range(0,12,1),labels=xticks_lable)
plt.legend(loc=(1,0))

plt.show()

