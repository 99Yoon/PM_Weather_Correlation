# PM_Weather_Correlation  
기상 요인에 따른 미세먼지 상관관계 분석

---

## 📌 프로젝트 목적
본 프로젝트는 국내 영향 및 기상 요인이 미세먼지 농도에 미치는 영향을 분석하고 시각화하는 것을 목표로 합니다.  
기상청 API를 기반으로 강수량, 기온, 습도, 대기압 등 다양한 기상 데이터를 불러와 미세먼지 농도와 비교 분석했으며, EDA(탐색적 데이터 분석)를 통해 의미 있는 패턴과 상관관계를 시각적으로 도출했습니다.  
이를 통해 미세먼지 농도에 가장 큰 영향을 미치는 요인을 식별하고, 일상생활에서 실용적으로 활용할 수 있는 조언을 제시하고자 했습니다.

---

## 👥 팀원 구성

| 팀원   | 역할                                      |
| ------ | ----------------------------------------- |
| 윤찬열 | 팀장, 데이터 전처리 및 분석, 발표자료 제작 |
| 김수명 | 기획서 작성, 데이터 전처리 및 분석        |
| 진예찬 | 데이터 전처리 및 분석, 발표자료 제작      |
| 서유찬 | 데이터 전처리 및 분석, 발표              |

---

## 📊 분석 결과

### 📍 주요 도시별 미세먼지 나쁨 비율

![주요 도시별 미세먼지 나쁨 비율](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/city_ratio.png)

---

### 🌧 강수량과 미세먼지 비교

![강수량과 미세먼지 비교](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/rain_pm.png)

---

### 💨 풍속과 미세먼지 상관관계

![풍속과 미세먼지 상관관계](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/windy.png)

---

### 📆 월별 PM10 농도

![월별 PM10 농도](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/month.png)

---

### 👥 인구밀도와 PM10 농도 관계

![인구밀도와 PM10농도 관계](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/people.png)

---

### 📍 위치 별 미세먼지 농도

![위치 별 미세먼지 농도](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/location.png)

- 위 그래프에서 **서쪽 지역의 미세먼지 농도가 동쪽 지역보다 높은 경향**이 확인됩니다.  
이는 중국 등 외부에서 유입되는 미세먼지가 국내 PM10 농도에 영향을 준 것으로 해석할 수 있습니다.

---

### 📈 연도별 미세먼지 평균

![연도별 미세먼지 평균](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/year.png)

- 해당 그래프는 2014년부터 현재까지의 **연도별 미세먼지 평균 농도 추이**를 보여줍니다.  
- 2014년부터 2019년까지 지속적인 감소세를 보였으나, **2022년 이후 다시 농도가 상승하는 경향**이 나타났습니다.  
- 이는 코로나19로 인해 가동이 중단되었던 일부 산업시설과 공장이 재가동되면서 PM10 배출량이 증가했기 때문으로 추정됩니다.

---

## 📌 참고
- 본 리포지토리는 **포트폴리오용 정리 버전**이며, 외부 API 호출이 만료된 데이터는 저장된 CSV 기반으로 분석이 진행됩니다.
- 이미지와 설명을 통해 결과를 직관적으로 확인할 수 있도록 구성했습니다.
