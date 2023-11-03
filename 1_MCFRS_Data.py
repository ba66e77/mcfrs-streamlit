import duckdb
import pandas as pd
import streamlit as st

# connect to db share 'md:_share/mcfrs/7aef3ea1-e3f1-4dfa-bbf8-afcd60347bc0'
c2 = duckdb.connect(f'md:?motherduck_token={st.secrets["motherduck"]["token"]}')
c2.sql("use mcfrs_share")

station_data = c2.sql("from overall_station_summary order by avg_monthly_incidents desc").fetchdf()

st.set_page_config(
	layout = 'wide'
)

st.markdown("# MCFRS Data")
st.dataframe(
	station_data, 
	hide_index=True,
	column_order = (
		'station_number',
		'station_name',
		'avg_monthly_incidents',
		'avg_pct_incidents_specified',
		'reported_months'
	)
)