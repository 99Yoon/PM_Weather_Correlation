# PM_Weather_Correlation
기상 요인에 따른 미세먼지 상관관계 분석



## 프로젝트 목적
국내 영향과 날씨 영향을 중심으로, 기상청 API를 활용해 강수량, 기온, 습도, 대기압 등 기상 데이터와 미세먼지 농도 간의 상관관계를 분석합니다.  
EDA(탐색적 데이터 분석)를 통해 기상 요인이 미세먼지 농도에 미치는 영향을 시각화하고, 가장 큰 영향을 미치는 요인을 식별합니다.  
이를 바탕으로 일상생활에서 활용 가능한 실용적인 조언을 도출하는 것이 최종 목표입니다.



## 팀원 구성 

| 팀원   | 역할                                      |
| ------ | ----------------------------------------- |
| 윤찬열 | 팀장, 데이터 전처리 및 분석, ppt      |
| 김수명 | 기획서 작성, 데이터 전처리 및 분석 |
| 진예찬 | 데이터 전처리 및 분석, ppt           |
| 서유찬 | 데이터 전처리 및 분석, 발표          |


## 결과

<H3> 주요 도시별 미세먼지 나쁨 비율 </H3>

![주요 도시별 미세먼지 나쁨 비율](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/city_ratio.png)

<H3> 강수량과 미세먼지 비교 </H3>

![강수량과 미세먼지 비교](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/rain_pm.png)

<H3> 풍속과 미세먼지 상관관계 </H3>

![풍속과 미세먼지 상관관계](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/windy.png)

<H3> 월별 PM10 농도 </H3>

![월별 PM10 농도](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/month.png)

<H3> 인구밀도와 PM10농도 관계 </H3>

![인구밀도와 PM10농도 관계](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/people.png)

<H3> 위치 별 미세먼지 농도 </H3>

![위치 별 미세먼지 농도](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/location.png)

-서쪽 지역의 미세먼지 농도가 동쪽 지역보다 높은 경향을 확인할 수 있습니다.  
이는 중국에서 유입되는 미세먼지가 우리나라 PM10 농도에 영향을 미치기 때문으로 추정할 수 있습니다.

<H3> 연도별 미세먼지 평균 </H3>

![연도별 미세먼지 평균](https://github.com/99Yoon/PM_Weather_Correlation/blob/main/result_images/year.png)

-그림은 연도별 미세먼지 평균 농도를 보여줍니다. 2014년부터 점차 농도가 감소하는 경향을 확인할 수 있습니다. 하지만 2022년부터는 다시 농도가 상승하기 시작했습니다. 이는 코로나로 인해 일시적으로 가동이 멈췄던 공장들이 다시 가동되면서 PM10 배출량이 증가한 것이 원인으로 추정됩니다.
