import streamlit as st

body = """
# README

This project provides analysis of the [MCRFS Incidents by Station data](https://data.montgomerycountymd.gov/Public-Safety/MCFRS-Incidents-by-Station/mf5d-mtzf) made available to the public by the county on [data.montgomerycountymd.gov](https://data.montgomerycountymd.gov). 

The project is implemented using [dbt](https://docs.getdbt.com) and [DuckDB](https://duckdb.org), running on the project owner's local machine. The `dbt` code used is publicly available in the [project GitLab repository](https://gitlab.com/ba66e77/mcfrs-data-exploration)

## Accessing compiled data
Access to the compiled data is provided through [MotherDuck](https://motherduck.com/). Access the database using [MotherDuck's share feature](https://motherduck.com/docs/motherduck-sql-reference/describe-share) and the db code `md:_share/mcfrs/7aef3ea1-e3f1-4dfa-bbf8-afcd60347bc0`



"""

st.markdown(body)