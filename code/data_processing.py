#!/usr/bin/env python
# coding: utf-8

# In[ ]:


loc_lst=['184','112','90','115','119','130','133','146','143','152','165','108','101','159','156'] # 사용할 지역 코드
url = f'https://apihub.kma.go.kr/api/typ01/url/kma_pm10.php?tm1=201401010000&tm2=201412312355&authKey=Fvf3FRRyTdG39xUUcv3RhA'
response = requests.get(url)

data_PM10 = response.text

cleaned_data_PM10 = []
for line in data_PM10.splitlines():
    if not line.startswith("#") and line.strip():
        cleaned_line = line.strip().rstrip(",=")
        cleaned_data_PM10.append(cleaned_line)

columns_PM10 = ["TM", "STN_ID", "PM10", "FLAG", "MQC"]

data_rows_PM10 = []
for line in cleaned_data_PM10: 
    split_line = re.split(r'\s*,\s*', line)
    if len(split_line) == 4:
        split_line.append("")
    if len(split_line) == 3:
        split_line.extend(["", ""])
    data_rows_PM10.append(split_line)

df_PM10 = pd.DataFrame(data_rows_PM10, columns=columns_PM10)

#이상데이터 제거
invalid_tm_entries = df_PM10[df_PM10['TM'].str.len() != 12]
df_PM10 = df_PM10[df_PM10['TM'].str.len() == 12]
    
    
    
#데이터 타입 정리
try: #datetime으로 변경하면서 오류가 생기는 값은 제외
    df_PM10["TM"] = pd.to_datetime(df_PM10["TM"], format='%Y%m%d%H%M')
except ValueError as e:
    print(f"Skipping row due to error: {e}")
df_PM10["STN_ID"] = df_PM10["STN_ID"].astype('str')
df_PM10["PM10"] = df_PM10["PM10"].astype('float')
df_PM10["FLAG"] = df_PM10["FLAG"].apply(lambda x: x.strip())
df_PM10["MQC"] = df_PM10["MQC"].apply(lambda x: x.strip())

df_PM10.drop(columns=['FLAG','MQC'],inplace=True)


for i in range(15,24):#데이터가 커서 연도별로 받아서 전처리 후 합
    
    url = f'https://apihub.kma.go.kr/api/typ01/url/kma_pm10.php?tm1=20{i}01010000&tm2=20{i}12312355&authKey=Fvf3FRRyTdG39xUUcv3RhA'
    response = requests.get(url)

    data_PM10dum = response.text

    cleaned_data_PM10dum = []
    for line in data_PM10dum.splitlines():
        if not line.startswith("#") and line.strip():
            cleaned_line = line.strip().rstrip(",=")
            cleaned_data_PM10dum.append(cleaned_line)

    columns_PM10 = ["TM", "STN_ID", "PM10", "FLAG", "MQC"]

    data_rows_PM10dum = []
    for line in cleaned_data_PM10dum:
        split_line = re.split(r'\s*,\s*', line)
        if len(split_line) == 4:
            split_line.append("")
        if len(split_line) == 3:
            split_line.extend(["", ""])
        data_rows_PM10dum.append(split_line)

    df_PM10dum = pd.DataFrame(data_rows_PM10dum, columns=columns_PM10)
    

    invalid_tm_entries = df_PM10dum[df_PM10dum['TM'].str.len() != 12]
    df_PM10dum = df_PM10dum[df_PM10dum['TM'].str.len() == 12]
    
    try: 
        df_PM10dum["TM"] = pd.to_datetime(df_PM10dum["TM"], format='%Y%m%d%H%M')
    except ValueError as e:
        print(f"Skipping row due to error: {e}")
        continue
    df_PM10dum["STN_ID"] = df_PM10dum["STN_ID"].astype('str')
    df_PM10dum["PM10"] = df_PM10dum["PM10"].astype('float')
    df_PM10dum["FLAG"] = df_PM10dum["FLAG"].apply(lambda x: x.strip())
    df_PM10dum["MQC"] = df_PM10dum["MQC"].apply(lambda x: x.strip())

    df_PM10dum.drop(columns=['FLAG','MQC'],inplace=True)

    df_PM10=pd.concat([df_PM10,df_PM10dum])
    
df_PM10_d=df_PM10.groupby([df_PM10['TM'].dt.date,'STN_ID']).
                mean(numeric_only=True).
                drop(columns='index').copy().reset_index()
        

##코드 정보 가져오기    

url='https://apihub.kma.go.kr/api/typ01/url/stn_inf.php?inf=SFC&stn=&tm=202211300900&help=0&authKey=Fvf3FRRyTdG39xUUcv3RhA'
r=requests.get(url)
data_inf=r.text

#데이터중 필요없는 부분 제거
start_index = data_inf.find("#START7777") + len("#START7777")
end_index = data_inf.find("#7777END")
extracted_data = data_inf[start_index:end_index].strip()

cleaned_data_inf = []
for line in extracted_data.splitlines():#데이터중 필요없는 부분 제거
    if not line.startswith("#") and line.strip():
        cleaned_line = line.strip()
        cleaned_data_inf.append(cleaned_line)

data_rows_inf = []
for line in cleaned_data_inf:#데이터 분류
    split_line = re.split(r'\s{1,}', line.strip())
    data_rows_inf.append(split_line)
    
for i in range(len(data_rows_inf)):#띄어쓰기 잘못된 데이터 처리
    if len(data_rows_inf[i])!= 15:
        data_rows_inf[i][11]=(str(data_rows_inf[i][11])+str(data_rows_inf[i][12]))
        data_rows_inf[i].pop(12)
        
columns_inf=['STN_ID','LON','LAT','STN_SP','HT','HT_PA','HT_TA','HT_WD','HT_RN','STN_CD','STN_KO','STN_EN','FCT_ID','LAW_ID','BASIN']
df_inf = pd.DataFrame(data_rows_inf, columns=columns_inf)

