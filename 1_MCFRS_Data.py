import duckdb
import pandas as pd
import streamlit as st

# connect to db share 'md:_share/mcfrs/7aef3ea1-e3f1-4dfa-bbf8-afcd60347bc0'
conn = duckdb.connect(f'md:?motherduck_token={st.secrets["motherduck"]["token"]}')
conn.sql("use mcfrs")

station_data = conn.sql("from overall_station_summary order by avg_monthly_incidents desc").fetchdf()

# Get the first and last report month, for display
# @todo: Add error handling for this query
max_min_query = """
select max(concat(year, lpad(month, 2,0))::int) as most_recent_report, 
min(concat(year, lpad(month, 2,0))::int) as first_report,
max(record_created) as last_update_date
from stg_incidents;
"""

max_report, min_report, latest_update = conn.execute(max_min_query).fetchone()

st.set_page_config(
	layout = 'wide'
)

st.markdown("# MCFRS Data")
st.markdown("## Average monthly incident counts for each station")
st.markdown(f"Based on data from **{min_report}** to **{max_report}**.")
st.markdown(f"Most recent update: *{latest_update}*")
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