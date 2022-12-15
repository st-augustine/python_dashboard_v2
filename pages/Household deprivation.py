# %%
import streamlit as st 
import plotly.express as px
import pandas as pd

# %%
def merge_spatial_data(gdf, df, left_on="", right_on=""):
    gdf=gdf.merge(df, left_on=left_on, right_on=right_on)
    return gdf

# %%
merged_wd_oa = st.session_state['merged_wd_oa']

# %%
#read in deprivation by oa dataset

try:
  deprivation_oa = pd.read_csv('lbth_census_2021_deprivation_oa.csv')
except:
  deprivation_oa = pd.read_csv('https://www.nomisweb.co.uk/api/v01/dataset/NM_2031_1.data.csv?date=latest&geography=629165479...629165982,629303674...629303812,629317322...629317326,629317336...629317343,629317349...629317360,629317362...629317366,629317371,629317374,629317376,629317378,629317379,629317381,629317385,629317388...629317392,629317394...629317397,629317399...629317403,629317405...629317407,629317409,629317411,629317412,629317416...629317420,629317422...629317424,629317426,629317429...629317434,629317436,629317437,629317440...629317442,629317444...629317450,629317452...629317456,629317459...629317461,629317463,629317466...629317468,629317472,629317474...629317479,629317481,629317483,629317486,629317487,629317490,629317492,629317494,629317495,629317497,629317499...629317502,629317504,629317505,629317507...629317509,629317512...629317514,629317517,629317520,629317523,629317525,629317527,629317531,629317534,629317535,629317537,629317538,629317540,629317543...629317548,629317551,629317554,629317555,629317558,629317560,629317562,629317563,629317565,629317566,629317569...629317573,629317576...629317578,629317580,629317582,629317584,629317585,629317587,629317590...629317592,629317594,629317596...629317599,629317601,629317603,629317604,629317606,629317607,629317610,629317612,629317613,629317615...629317617,629317619...629317621,629317623,629317625...629317629,629317631...629317634,629317636,629317640,629317648,629317650...629317659,629317662,629317663,629317666...629317669,629317672...629317687,629317689,629317691,629317694,629317695,629317697,629317698,629317700,629317701,629317703,629317704,629317706,629317707,629317711...629317714,629317716,629317718...629317720,629317722...629317724,629317726,629317729,629317731,629317733,629317736...629317742,629317744,629317746...629317748,629323624,629323625&c2021_dep_6=0...5&measures=20100,20301&select=date_name,geography_name,geography_code,c2021_dep_6_name,measures_name,obs_value,obs_status_name')
  deprivation_oa.to_csv('lbth_census_2021_deprivation_oa.csv')

#merge deprivation data with spatial data
deprivation_merge=merge_spatial_data(merged_wd_oa, deprivation_oa,"OA21CD", "GEOGRAPHY_CODE")

# %%
st.header('Household deprivation')
page= st.sidebar.selectbox('Select variable',
  ['Household is not deprived in any dimension','Household is deprived in one dimension','Household is deprived in two dimensions',
  'Household is deprived in three dimensions','Household is deprived in four dimensions'])


if page =='Household is not deprived in any dimension': 
 deprivation_merge= deprivation_merge[deprivation_merge.MEASURES_NAME == 'Value']
 deprivation_merge = deprivation_merge[deprivation_merge["C2021_DEP_6_NAME"].str.contains('Household is not deprived in any dimension') == True]
 fig = px.choropleth(deprivation_merge.dissolve(by='ward_name'),
                   geojson=deprivation_merge.dissolve(by='ward_name').geometry,
                   locations=deprivation_merge.dissolve(by='ward_name').index,
                   color="OBS_VALUE",
                   color_continuous_scale = 'viridis_r',
                   projection="mercator",
                   hover_name=deprivation_merge.dissolve(by='ward_name').index,
                   hover_data=['OBS_VALUE'])
 fig.update_geos(fitbounds="locations", visible=False)
 st.plotly_chart(fig,use_container_width = True)

elif page =='Household is deprived in one dimension': 
 deprivation_merge= deprivation_merge[deprivation_merge.MEASURES_NAME == 'Value']
 deprivation_merge = deprivation_merge[deprivation_merge["C2021_DEP_6_NAME"].str.contains('Household is deprived in one dimension') == True]
 fig = px.choropleth(deprivation_merge.dissolve(by='ward_name'),
                   geojson=deprivation_merge.dissolve(by='ward_name').geometry,
                   locations=deprivation_merge.dissolve(by='ward_name').index,
                   color="OBS_VALUE",
                   color_continuous_scale = 'viridis_r',
                   projection="mercator",
                   hover_name=deprivation_merge.dissolve(by='ward_name').index,
                   hover_data=['OBS_VALUE'])
 fig.update_geos(fitbounds="locations", visible=False)
 st.plotly_chart(fig,use_container_width = True)

elif page =='Household is deprived in two dimensions': 
 deprivation_merge= deprivation_merge[deprivation_merge.MEASURES_NAME == 'Value']
 deprivation_merge = deprivation_merge[deprivation_merge["C2021_DEP_6_NAME"].str.contains('Household is deprived in two dimensions') == True]
 fig = px.choropleth(deprivation_merge.dissolve(by='ward_name'),
                   geojson=deprivation_merge.dissolve(by='ward_name').geometry,
                   locations=deprivation_merge.dissolve(by='ward_name').index,
                   color="OBS_VALUE",
                   color_continuous_scale = 'viridis_r',
                   projection="mercator",
                   hover_name=deprivation_merge.dissolve(by='ward_name').index,
                   hover_data=['OBS_VALUE'])
 fig.update_geos(fitbounds="locations", visible=False)
 st.plotly_chart(fig,use_container_width = True)

elif page =='Household is deprived in three dimensions': 
 deprivation_merge= deprivation_merge[deprivation_merge.MEASURES_NAME == 'Value']
 deprivation_merge = deprivation_merge[deprivation_merge["C2021_DEP_6_NAME"].str.contains('Household is deprived in three dimensions') == True]
 fig = px.choropleth(deprivation_merge.dissolve(by='ward_name'),
                   geojson=deprivation_merge.dissolve(by='ward_name').geometry,
                   locations=deprivation_merge.dissolve(by='ward_name').index,
                   color="OBS_VALUE",
                   color_continuous_scale = 'viridis_r',
                   projection="mercator",
                   hover_name=deprivation_merge.dissolve(by='ward_name').index,
                   hover_data=['OBS_VALUE'])
 fig.update_geos(fitbounds="locations", visible=False)
 st.plotly_chart(fig,use_container_width = True)

elif page== 'Household is deprived in four dimensions':
 deprivation_merge= deprivation_merge[deprivation_merge.MEASURES_NAME == 'Value']
 deprivation_merge = deprivation_merge[deprivation_merge["C2021_DEP_6_NAME"].str.contains('Household is deprived in four dimensions') == True]
 fig = px.choropleth(deprivation_merge.dissolve(by='ward_name'),
                   geojson=deprivation_merge.dissolve(by='ward_name').geometry,
                   locations=deprivation_merge.dissolve(by='ward_name').index,
                   color="OBS_VALUE",
                   color_continuous_scale = 'viridis_r',
                   projection="mercator",
                   hover_name=deprivation_merge.dissolve(by='ward_name').index,
                   hover_data=['OBS_VALUE'])
 fig.update_geos(fitbounds="locations", visible=False)
 st.plotly_chart(fig,use_container_width = True)


