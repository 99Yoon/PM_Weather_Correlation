#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## 속초 미세먼지 농도구간별 평균 강수량

df_PM_rain_sok=df_PM[df_PM['STN_KO']=='속초'].copy()
df_rain_sok=df_rela[['관측일','국내 지점번호','일 강수량']]
df_rain_sok = df_rain_sok[df_rain_sok['국내 지점번호']=='90'].copy()
df_rain_sok['관측일'] = df_rain_sok['관측일'].astype('str')

df_PM_rain_sok['TM'] = pd.to_datetime(df_PM_rain_sok['TM']).dt.strftime('%Y-%m-%d')
df_rain_sok['관측일'] = pd.to_datetime(df_rain_sok['관측일']).dt.strftime('%Y-%m-%d')
df_PM_rain_sok=pd.merge(df_PM_rain_sok,df_rain_sok,left_on=['TM','STN_ID'],right_on=['관측일','국내 지점번호'])
df_PM_rain_sok = df_PM_rain_sok.drop(columns=['TM', 'STN_ID','국내 지점번호'])
df_PM_rain_sok.loc[df_PM_rain_sok['일 강수량'] == '-9.0', '일 강수량'] = '0'
df_PM_rain_sok['일 강수량']=df_PM_rain_sok['일 강수량'].astype('float64')

df_PMrain_sok=pd.DataFrame(columns=['PM10농도','평균 강수량'])
for i in range(20,80,20):
    dum = pd.DataFrame({'PM10농도': [str(i)+'~'+str(i+20)],
                        '평균 강수량': [df_PM_rain_sok[(df_PM_rain_sok['PM10'] > i)&(df_PM_rain_sok['PM10']<=i+20)]['일 강수량'].mean()]})
    df_PMrain_sok=pd.concat([df_PMrain_sok,dum])
dum = pd.DataFrame({'PM10농도': ['80~'],
                    '평균 강수량': [df_PM_rain_sok[df_PM_rain_sok['PM10'] > 80]['일 강수량'].mean()]})
df_PMrain_sok=pd.concat([df_PMrain_sok,dum])
df_PMrain_sok.reset_index(drop=True,inplace=True)





## 대구 미세먼지 농도구간별 평균 강수량

df_PM_rain_dae=df_PM[df_PM['STN_KO']=='대구'].copy()
df_rain_dae=df_rela[['관측일','국내 지점번호','일 강수량']]
df_rain_dae= df_rain_dae[df_rain_dae['국내 지점번호']=='143'].copy()
df_rain_dae['관측일'] = df_rain_dae['관측일'].astype('str')

df_PM_rain_dae['TM'] = pd.to_datetime(df_PM_rain_dae['TM']).dt.strftime('%Y-%m-%d')
df_rain_dae['관측일'] = pd.to_datetime(df_rain_dae['관측일']).dt.strftime('%Y-%m-%d')
df_PM_rain_dae=pd.merge(df_PM_rain_dae,df_rain_dae,left_on=['TM','STN_ID'],right_on=['관측일','국내 지점번호'])
df_PM_rain_dae = df_PM_rain_dae.drop(columns=['TM', 'STN_ID','국내 지점번호'])
df_PM_rain_dae.loc[df_PM_rain_dae['일 강수량'] == '-9.0', '일 강수량'] = '0'
df_PM_rain_dae['일 강수량']=df_PM_rain_dae['일 강수량'].astype('float64')

df_PMrain_dae=pd.DataFrame(columns=['PM10농도','평균 강수량'])
for i in range(20,80,20):
    dum = pd.DataFrame({'PM10농도': [str(i)+'~'+str(i+20)],
                        '평균 강수량': [df_PM_rain_dae[(df_PM_rain_dae['PM10'] > i)&(df_PM_rain_dae['PM10']<=i+20)]['일 강수량'].mean()]})
    df_PMrain_dae=pd.concat([df_PMrain_dae,dum])
dum = pd.DataFrame({'PM10농도': ['80~'],
                    '평균 강수량': [df_PM_rain_dae[df_PM_rain_dae['PM10'] > 80]['일 강수량'].mean()]})
df_PMrain_dae=pd.concat([df_PMrain_dae,dum])
df_PMrain_dae.reset_index(drop=True,inplace=True)





##전주 미세먼지 농도구간별 평균 강수량

df_PM_rain_jun=df_PM[df_PM['STN_KO']=='전주'].copy()
df_rain_jun=df_rela[['관측일','국내 지점번호','일 강수량']]
df_rain_jun = df_rain_jun[df_rain_jun['국내 지점번호']=='146'].copy()
df_rain_jun['관측일'] = df_rain_jun['관측일'].astype('str')

df_PM_rain_jun['TM'] = pd.to_datetime(df_PM_rain_jun['TM']).dt.strftime('%Y-%m-%d')
df_rain_jun['관측일'] = pd.to_datetime(df_rain_jun['관측일']).dt.strftime('%Y-%m-%d')
df_PM_rain_jun=pd.merge(df_PM_rain_jun,df_rain_jun,left_on=['TM','STN_ID'],right_on=['관측일','국내 지점번호'])
df_PM_rain_jun = df_PM_rain_jun.drop(columns=['TM', 'STN_ID','국내 지점번호'])
df_PM_rain_jun.loc[df_PM_rain_jun['일 강수량'] == '-9.0', '일 강수량'] = '0'
df_PM_rain_jun['일 강수량']=df_PM_rain_jun['일 강수량'].astype('float64')

df_PMrain_jun=pd.DataFrame(columns=['PM10농도','평균 강수량'])
for i in range(20,80,20):
    dum = pd.DataFrame({'PM10농도': [str(i)+'~'+str(i+20)],
                        '평균 강수량': [df_PM_rain_jun[(df_PM_rain_jun['PM10'] > i)&(df_PM_rain_jun['PM10']<=i+20)]['일 강수량'].mean()]})
    df_PMrain_jun=pd.concat([df_PMrain_jun,dum])
dum = pd.DataFrame({'PM10농도': ['80~'],
                    '평균 강수량': [df_PM_rain_jun[df_PM_rain_jun['PM10'] > 80]['일 강수량'].mean()]})
df_PMrain_jun=pd.concat([df_PMrain_jun,dum])
df_PMrain_jun.reset_index(drop=True,inplace=True)




## 서울 미세먼지 농도구간별 평균 강수량

df_PM_rain_seo=df_PM[df_PM['STN_KO']=='서울'].copy()
df_rain_seo=df_rela[['관측일','국내 지점번호','일 강수량']]
df_rain_seo = df_rain_seo[df_rain_seo['국내 지점번호']=='108'].copy()
df_rain_seo['관측일'] = df_rain_seo['관측일'].astype('str')

df_PM_rain_seo['TM'] = pd.to_datetime(df_PM_rain_seo['TM']).dt.strftime('%Y-%m-%d')
df_rain_seo['관측일'] = pd.to_datetime(df_rain_seo['관측일']).dt.strftime('%Y-%m-%d')
df_PM_rain_seo=pd.merge(df_PM_rain_seo,df_rain_seo,left_on=['TM','STN_ID'],right_on=['관측일','국내 지점번호'])
df_PM_rain_seo = df_PM_rain_seo.drop(columns=['TM', 'STN_ID','국내 지점번호'])
df_PM_rain_seo['일 강수량']=df_PM_rain_seo['일 강수량'].astype('float64')

df_PMrain_seo=pd.DataFrame(columns=['PM10농도','평균 강수량'])
for i in range(20,80,20):
    dum = pd.DataFrame({'PM10농도': [str(i)+'~'+str(i+20)],
                        '평균 강수량': [df_PM_rain_seo[(df_PM_rain_seo['PM10'] > i)
                                                  &(df_PM_rain_seo['PM10']<=i+20)]['일 강수량'].mean()]})
    df_PMrain_seo=pd.concat([df_PMrain_seo,dum])
dum = pd.DataFrame({'PM10농도': ['80~'],
                    '평균 강수량': [df_PM_rain_seo[df_PM_rain_seo['PM10'] > 80]['일 강수량'].mean()]})
df_PMrain_seo=pd.concat([df_PMrain_seo,dum])
df_PMrain_seo.reset_index(drop=True,inplace=True)


## 시각화

x = np.arange(len(df_PMrain_seo['PM10농도']))
width = 0.2  

plt.bar(x - width, df_PMrain_seo['평균 강수량'], width=width, label='서울')
plt.bar(x, df_PMrain_dae['평균 강수량'], width=width, label='대구')
plt.bar(x + width, df_PMrain_jun['평균 강수량'], width=width, label='전주')
plt.bar(x + 2*width, df_PMrain_sok['평균 강수량'], width=width, label='속초')

plt.xticks(x, df_PMrain_seo['PM10농도'])
plt.legend()
plt.title('PM10농도별 평균 강수량 ',pad='15')
plt.xlabel('PM10농도(µg/m³)')
plt.ylabel('평균 강수량(mm)')
plt.grid(ls=':', alpha=0.8, axis='y')
plt.show()

