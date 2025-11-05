# geovisualization.py
# 지도 시각화

# 파이참에서 웹브라우저에 지도 표시하는 함수
import webbrowser
def browser_open(f_map, path):
    html_page = f'{path}'
    f_map.save(html_page)
    webbrowser.open(html_page)

# 대한민국 시군구 경계 좌표
import json
geo = json.load(open('./assets/SIG.geojson', encoding='utf-8'))
# print(geo)

# 행정구역 코드, 영문명, 한글명
# print(geo['features'][0]['properties'])

# 위도, 경도 좌표
# print(geo['features'][0]['geometry'])

# 시군구별 인구데이터
import pandas as pd
df_pop = pd.read_csv('./assets/Population_SIG.csv')
print(df_pop.head())
df_pop.info()

# code를 문자타입으로 변경
df_pop['code'] = df_pop['code'].astype(str)
df_pop.info()

# 단계구분도 생성
import folium

# 맵 UI
map_sig = folium.Map(
    location = [35.95, 127.7], # 중심 위/경도
    zoom_start = 8, # 확대레벨
    tiles = 'cartodbpositron' # 지도맵디자인유형
)

# 맵 UI에 맵 데이터 매핑
# folium.Choropleth(
#     geo_data = geo, # 지형 데이터
#     data = df_pop, # 지형에 표시할 데이터
#     columns = ('code', 'pop'), # 행정구역코드, 인구
#     key_on = 'feature.properties.SIG_CD' # 행정구역코드
# ).add_to(map_sig)
#
# browser_open(map_sig, 'geo1.html')

# 계급구간 정하기
bins = list(df_pop['pop'].quantile([0, 0.2, 0.4, 0.6, 0.8, 1.0]))
# print(bins)

folium.Choropleth(
    geo_data = geo, # 지형 데이터
    data = df_pop, # 지형에 표시할 데이터
    columns = ('code', 'pop'), # 행정구역코드, 인구
    key_on = 'feature.properties.SIG_CD', # 행정구역코드
    fill_color='YlGnBu',
    fill_opacity = 0.5,
    line_opacity = 0.5,
    bins = bins
).add_to(map_sig)

browser_open(map_sig, 'geo2.html')

















































