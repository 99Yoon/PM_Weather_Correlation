#!/usr/bin/env python
# coding: utf-8

# In[ ]:


df_rela_ws=df_rela[['관측일','국내 지점번호','일 평균 풍속']]

## 데이터 프레임 병합 후 정리 
df_PM_ws=df_PM.copy()
df_PM_ws['TM'] = pd.to_datetime(df_PM_ws['TM']).dt.strftime('%Y-%m-%d')
df_rela_ws = df_rela_ws.copy()
df_rela_ws['관측일'] = pd.to_datetime(df_rela_ws['관측일']).dt.strftime('%Y-%m-%d')
df_ws_avg=pd.merge(df_PM_ws,df_rela_ws,left_on=['TM','STN_ID'],right_on=['관측일','국내 지점번호'])
df_ws_avg.drop(columns=['TM','STN_ID'],inplace=True)
df_ws_avg['일 평균 풍속']=df_ws_avg['일 평균 풍속'].astype('float64')

ws_uni=df_ws_avg['STN_KO'].unique()

df_ws_avg_jun=df_ws_avg[df_ws_avg['STN_KO']=='전주']
df_ws_avg_ul=df_ws_avg[df_ws_avg['STN_KO']=='울산']
df_ws_avg_back=df_ws_avg[df_ws_avg['STN_KO']=='백령도']
df_ws_avg_sock=df_ws_avg[df_ws_avg['STN_KO']=='속초']

## 시각화

plt.figure(figsize=(10, 6))
for i in ws_uni:
    plt.scatter(df_ws_avg[df_ws_avg['STN_KO']==i]['일 평균 풍속'],
                df_ws_avg[df_ws_avg['STN_KO']==i]['PM10'],
                alpha=0.6,label=i)
plt.ylabel('PM10농도(µg/m³)',labelpad=10,size=15)
plt.xlabel('일 평균 풍속(m/s)',labelpad=10,size=15)
plt.title('풍속과 미세먼지 상관관계',pad=15,size=20)
plt.legend(loc=(1,0))
plt.show()

