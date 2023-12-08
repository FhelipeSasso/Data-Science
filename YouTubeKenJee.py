import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

# loading data                                # skip the first row   
df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]
df_agg.columns = ['Video', 'Video title', 'Video publish time', 'Comments added', 'Shares', 
                  'Dislikes', 'Likes', 'Subscribers lost', 'Subscribers gained', 'RPM(USD)',
                  'CPM(USD)','Average % viewed', 'Average view duration','Views', 'Watch time (hours)', 'Subscribers',
                  'Your estimated revenue (USD)', 'Impressions', 'Impresions ctr(%)']

df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time'])
df_agg['Average view duration'] = df_agg['Average view duration'].apply(lambda x: datetime.strptime(x, '%H.%M.%S'))
df_agg['Avg_duration_sec'] = df_agg['Average view duration'].apply(lambda x: x.second + x.minutes*60 + x.hour*3600)
df_agg['Engagement_ratio'] = df_agg['Comments...']


df_agg_sub = pd.read_csv('Aggregated_Metrics_By_Country_And_Subscribers_Status.csv')
df_comments = pd.read_csv('Aggregated_Metrics_By_Video.csv')
df_time = pd.read_csv('Aggregated_Metrics_By_Video.csv')
# 17:26
# em progresso