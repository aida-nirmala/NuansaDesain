import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

def daftar_rekomendasi():
    st.title('Daftar Rekomendasi Warna')

    def fetch_data_from_db(query):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_rekomendasi'
            )
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            df = pd.DataFrame(result, columns=columns)
        except Error as e:
            st.error(f"Error: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        return df

    st.subheader('Data Warna')
    query_data_warna = "SELECT * FROM data_warna"
    df_asli = fetch_data_from_db(query_data_warna)
    st.markdown(df_asli.to_html(index=False), unsafe_allow_html=True)

    st.subheader('Data Kombinasi')
    query_data_kombinasi = "SELECT * FROM data_kombinasi"
    df_kombinasi = fetch_data_from_db(query_data_kombinasi)
    st.markdown(df_kombinasi.to_html(index=False), unsafe_allow_html=True)

if __name__ == '__main__':
    daftar_rekomendasi()
