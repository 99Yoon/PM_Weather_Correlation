#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## 인구 데이터 받아오기
url='https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json'

key_res = requests.get(url,params={'consumer_key':consumer_key,'consumer_secret':consumer_secret})
r_data = key_res.json()
access_token = r_data['result']['accessToken']

# 서울,광역시 데이터
url='https://sgisapi.kostat.go.kr/OpenAPI3/stats/population.json'
ingu_res=requests.get(url,params={'accessToken':access_token,'year':'2022','low_search':'2'})
ingu_data=ingu_res.json()

#강화 데이터
url='https://sgisapi.kostat.go.kr/OpenAPI3/stats/population.json'
ingu_res_gang=requests.get(url,params={'accessToken':access_token,
                                       'year':'2022','low_search':'0','adm_cd':'23510'})
ingu_data_gang=ingu_res_gang.json()
df_gang=pd.DataFrame(ingu_data_gang['result'])
df_gang=df_gang[['adm_nm','ppltn_dnsty']]
df_gang.columns=['STN_KO','인구밀도']
df_gang['인구밀도']=df_gang['인구밀도'].astype('float64')

df_gang['STN_KO'] = '강화'
df_gang = df_gang.groupby('STN_KO')['인구밀도'].mean().reset_index()

#군산 데이터
url='https://sgisapi.kostat.go.kr/OpenAPI3/stats/population.json'
ingu_res_goon=requests.get(url,params={'accessToken':access_token,'year':'2022','low_search':'0','adm_cd':'35020'})
ingu_data_goon=ingu_res_goon.json()
df_goon=pd.DataFrame(ingu_data_goon['result'])
df_goon=df_goon[['adm_nm','ppltn_dnsty']]
df_goon.columns=['STN_KO','인구밀도']
df_goon['인구밀도']=df_goon['인구밀도'].astype('float64')

df_goon['STN_KO'] = '군산'
df_goon = df_goon.groupby('STN_KO')['인구밀도'].mean().reset_index()

# 수원 데이터
url='https://sgisapi.kostat.go.kr/OpenAPI3/stats/population.json'
ingu_res_su=requests.get(url,params={'accessToken':access_token,'year':'2022','low_search':'1','adm_cd':'31'})
ingu_data_su=ingu_res_su.json()
df_su=[item for item in ingu_data_su['result'] if '수원시' in item['adm_nm']]
df_su=pd.DataFrame(df_su)
df_su=df_su[['adm_nm','ppltn_dnsty']]
df_su.columns=['STN_KO','인구밀도']
df_su['인구밀도']=df_su['인구밀도'].astype('float64')

df_su['STN_KO'] = '수원'
df_su = df_su.groupby('STN_KO')['인구밀도'].mean().reset_index()

#속초 데이터
url='https://sgisapi.kostat.go.kr/OpenAPI3/stats/population.json'
ingu_res_sok=requests.get(url,params={'accessToken':access_token,'year':'2022','low_search':'0','adm_cd':'32060'})
ingu_data_sok=ingu_res_sok.json()
df_sok=pd.DataFrame(ingu_data_sok['result'])
df_sok=df_sok[['adm_nm','ppltn_dnsty']]
df_sok.columns=['STN_KO','인구밀도']
df_sok['인구밀도']=df_sok['인구밀도'].astype('float64')

df_sok['STN_KO'] = '속초'
df_sok = df_sok.groupby('STN_KO')['인구밀도'].mean().reset_index()

#울릉도 데이터
ingu_res_ulleung=requests.get(url,params={'accessToken':access_token,'year':'2022','low_search':'0','adm_cd':'37630'})
ingu_data_ulleung=ingu_res_ulleung.json()
df_ulleung=pd.DataFrame(ingu_data_ulleung['result'])
df_ulleung=df_ulleung[['adm_nm','ppltn_dnsty']]
df_ulleung.columns=['STN_KO','인구밀도']
df_ulleung['인구밀도']=df_ulleung['인구밀도'].astype('float64')

df_ulleung['STN_KO'] = '울릉도'
df_ulleung = df_ulleung.groupby('STN_KO')['인구밀도'].mean().reset_index()

## 평균 데이터 병합 후 데이터프레임생성
df_ingu=pd.DataFrame(ingu_data['result'])
df_ingu_den=df_ingu[['adm_nm','ppltn_dnsty']]
df_ingu_den.columns=['STN_KO','인구밀도']
inhu_lst=['서울특별시','대구광역시','광주광역시','울산광역시']
df_ingu_den=df_ingu_den[df_ingu_den['STN_KO'].isin(inhu_lst)]
df_ingu_den['STN_KO'] = df_ingu_den['STN_KO'].replace({'서울특별시':'서울', '대구광역시':'대구', '광주광역시':'광주', '울산광역시':'울산'})
df_ingu_den=pd.concat([df_ingu_den,df_sok,df_su,df_ulleung,df_gang,df_goon])

df_year=df_PM.groupby(['STN_ID','STN_KO']).mean(numeric_only=True).reset_index()
df_ingu_den=pd.merge(df_ingu_den,df_year)
df_ingu_den['인구밀도']=df_ingu_den['인구밀도'].astype('float64')

## 시각화
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(df_ingu_den['STN_KO'],df_ingu_den['인구밀도'], width=0.5,color='skyblue',label='인구밀도')

ax2 = ax1.twinx()
ax2.plot(df_ingu_den['STN_KO'],df_ingu_den['PM10'], marker='o', ls='-.', label='PM10농도',color='r')

plt.title('인구밀도와 PM10 농도 간의 관계',pad=15,size=20)

ax1.set_xlabel('지역',size=15)
ax1.set_ylabel('인구밀도 (명/km²)')
ax2.set_ylabel('PM10 농도 (µg/m³)')
ax1.legend(loc='upper right')
ax2.legend(loc='upper left')
plt.show()

