import streamlit as st
st.title("Snowflake Data-App")

import pandas as pd
import snowflake.connector
conn = snowflake.connector.connect(
                user='VARSHINI',
                password='Snowflake@22!',
                account='bv18063.ap-southeast-1',
    ocsp_fail_open=False
                )


