#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## 좌표 별 평균
df_len=pd.merge(df_inf[['STN_ID','STN_KO','LON','LAT']],df_PM10_d)
df_len=df_len.groupby(['STN_KO','LON','LAT']).mean('PM10').reset_index()

## 시각화

gdf = gpd.GeoDataFrame(df_len, geometry=gpd.points_from_xy(df_len.LON, df_len.LAT))

gdf.set_crs(epsg=4326, inplace=True)
gdf = gdf.to_crs(epsg=5179)

fig, ax = plt.subplots(figsize=(10, 10))

norm = plt.Normalize(vmin=gdf['PM10'].min(), vmax=gdf['PM10'].max())
cmap = plt.cm.Reds 
sc = ax.scatter(gdf.geometry.x, gdf.geometry.y, s=(gdf['PM10']-20)*100,
                c=gdf['PM10'], cmap=cmap, norm=norm, alpha=0.6)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.CartoDB.Positron)

cbar = plt.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('PM10 농도')

plt.title('PM10 측정 위치 지도',size=20,pad=15)
ax.set_axis_off()
plt.show()

