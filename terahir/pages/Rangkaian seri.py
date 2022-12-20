import streamlit as st
st.title("hitung rangkaian seri")

#RANGKAIAN SERI

R1 = st.number_input ("Masukkan nilai hambatan R1", 0)
R2 = st.number_input ("Masukkan nilai hambatan R2", 0)




hitung = st.button ("Hitung: ",)

if hitung:
    RT = R1+R2    
    st.success(f"Hambatannya adalah {RT}")
    st.snow()