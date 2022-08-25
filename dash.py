import time  # to simulate a real time data, time loop
import pandas as pd  # read csv, df manipulation
import ssl
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

df = pd.read_csv("fakedataset.csv")

ssl._create_default_https_context = ssl._create_unverified_context

st.set_page_config(
    page_title="VIKAS Dashboard",
    page_icon="✅",
    layout="wide",
)

landmarks = ['kc', 'tiger circle', 'coin circle', 'malpe', 'hoode', 'kapu', 'nit surathkal', 'kundapura', 'karkala']

# dashboard title
st.title("VIKAS Dashboard")

# creating a single-element container
placeholder = st.empty()

classes = ['Caution and Advice\t', 'Displaced People and Evacuations\t', 
                'Donation Needs/Offers/Volunteers\t', 'Structural and Utilities Damage\t',
                'Injured or Dead People\t', 'Missing/Trapped/Found People\t',
                'Unrelated/Irrelevant\t', 'Other Useful Information\t',
                'Sympathy and Emotional Support\t']

fig = px.bar(x=[3, 3, 6, 5, 12, 17, 2, 1, 1], y=classes, orientation='h', color_discrete_sequence=["#94d2bd"])
fig.update_layout(title_text='<b>Resources Needed</b>', height=600, width=1200, title_x=0.6, title_y=1, title={'font': {'size': 25}})
st.write(fig)

fig = px.bar(x=[17, 12, 6, 5, 3, 3, 2, 1, 1], y=landmarks, orientation='h', color_discrete_sequence=["#94d2bd"])
fig.update_layout(title_text='<b>Location Analysis</b>', height=600, width=1200, title_x=0.6, title_y=1, title={'font': {'size': 25}})
st.write(fig)

st.markdown("### Data")
st.dataframe(df)

tweets = 0
text = 0
imgs = 0

# near real-time / live feed simulation
for seconds in range(72):

    with placeholder.container():

        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(label="Tweets Scraped",
            value=int(tweets),
            delta=+1,
        )
        
        kpi2.metric(label="Relevant Text",
            value=int(text),
            delta=+1,
        )
        
        kpi3.metric(
            label="Relevant Images",
            value=int(imgs),
            delta=+1,
        )

        # create two columns for charts
        st.text('\n\n')

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            fig = px.bar(x=['Mild', 'Severe'], y=[20, 9], color=['Mild', 'Severe'], color_discrete_sequence=["#94d2bd", "#0a9396"])
            fig.update_layout(title_text='<b>Severity</b>', title_x=0.5, title_y=1, title={'font': {'size': 25}}, showlegend=False)
            fig.update_traces(width=0.5)
            st.write(fig)
            
        with fig_col2:
            fig2 = px.bar(x=['Flood', 'Structural'], y=[7, 22], color=['Flood', 'Structural'], color_discrete_sequence=["#94d2bd", "#0a9396"])
            fig2.update_layout(title_text='<b>Type of Disaster</b>', title_x=0.5, title_y=1, title={'font': {'size': 25}}, showlegend=False)
            fig2.update_traces(width=0.5)
            st.write(fig2)

        tweets += 1
        if imgs<28:
            imgs += 1
        if text<50:
            text += 1
        time.sleep(0.0001)

