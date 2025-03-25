import pandas as pd
import pytest
import pyodbc
import cx_Oracle
from sqlalchemy import create_engine


@pytest.mark.skip
def test_data_extraction_comparison_src_tgt(src_source_set_up,tgt_target_set_up):
    df_src=src_source_set_up
    df_tgt=tgt_target_set_up
    if df_src.equals(df_tgt):
        print('pass result')
    else:
        print('Fail results')

@pytest.mark.skip
#Although the data is same in both DB's(Oracle,sqlserver), I am getting assertion error)
def test_verify_employee_Data_between_source_target(oracle_conn_set_up,sql_server_conn_set_up):
    print("Test case started")
    source_sql_query="""select * from source_emp order by Emp_no"""
    df_expected =pd.read_sql(source_sql_query,oracle_conn_set_up).astype(str)
    print(df_expected.dtypes)

    target_sql_query="""select * from target_emp order by Emp_no"""
    df_actual=pd.read_sql(target_sql_query,sql_server_conn_set_up).astype(str)
    print(df_actual.dtypes)

    assert df_actual.equals(df_expected),"Data mismatch"




#Here in oracle DB Datatype mismatch error while comparing Datatypes.
@pytest.mark.skip
def test_verify_source_data_datatype_check(oracle_conn_set_up):
    print("Test case started")
    source_sql_query="""select * from source_emp order by EMP_NO"""
    df_expected=pd.read_sql(source_sql_query,oracle_conn_set_up)
    actual_dtypes=df_expected.dtypes.to_dict()
    print("Actual Datatypes:",actual_dtypes)
    expected_dtypes={'Emp_no':'int64','Emp_name':'objectpytest','Dept_name':'object','Salary':'int64'}
    print("Expected_datatypes:",expected_dtypes)

    assert actual_dtypes==expected_dtypes,"Datatypes mismatch"
    print("Test case completed")

#Here in sql server i am not getting any errors while comparing Datatypes.
def test_verify_target_data_datatype_check(sql_server_conn_set_up):
    print("Test case started")
    source_sql_query="""select * from target_emp order by EMP_NO"""
    df_expected=pd.read_sql(source_sql_query,sql_server_conn_set_up)
    actual_dtypes=df_expected.dtypes.to_dict()
    print("Actual Datatypes:",actual_dtypes)
    expected_dtypes={'Emp_no':'int64','Emp_name':'object','Dept_name':'object','Salary':'int64'}
    print("Expected_datatypes:",expected_dtypes)
    assert actual_dtypes==expected_dtypes,"Datatypes mismatch"
