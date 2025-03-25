import pandas as pd
import pytest
import cx_Oracle
import pyodbc
from sqlalchemy import create_engine



@pytest.fixture()
def src_source_set_up():
    df_src = pd.read_csv("D:/ETL/Source.csv", sep=',')
    print("Source file reading before code execution")
    yield df_src
    print("Source file reading execution completed")

@pytest.fixture()
def tgt_target_set_up():
    df_tgt=pd.read_csv("D:/ETL/Target.csv",sep=',')
    print("target file reading before code execution ")
    yield df_tgt
    print("Target file reading execution completed successfully loaded")

@pytest.fixture()
def oracle_conn_set_up():
    engine = create_engine("oracle+cx_oracle://hr:Krish@localhost:1521/xe")
    connection_oracle = engine.connect()
    print("Oracle connection established")
    yield connection_oracle
    connection_oracle.close()
    print("Oracle connection closed")

@pytest.fixture()
def sql_server_conn_set_up():
    server = "LAPTOP-NQTOGKUH\SQLEXPRESS"
    Database = "master"
    driver = "ODBC Driver 17 for SQL SERVER"

    engine = create_engine(f"mssql+pyodbc://@{server}/{Database}?driver={driver}&trusted_connection=yes")
    connection_sql_server = engine.connect()
    print("SQL_Server connection established")
    yield connection_sql_server
    connection_sql_server.close()
    print("sql_server connection closed")
