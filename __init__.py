import os
import logging
import polars as pl
import pandas as pd
import sqlalchemy as sa
import streamlit as st
import lazypredict as lz
import streamlit as st
st.header("CrateDB connector and data exporter")
st.header("Universitat Potsdam")
username = st.text_input("Username", "username")
password = st.text_input("Password", "password")
localhost = st.text_input("Localhost", "localhost")
st.button("submit")
