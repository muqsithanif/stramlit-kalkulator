import streamlit as st
st.title("hitung Hambatan listrik")

# Menampilkan form untuk memasukkan nilai tegangan dan arus
voltage = st.number_input("Masukkan nilai tegangan (dalam volt):", 0)

current = st.number_input("Masukkan nilai arus (dalam ampere):", 0)


hitung = st.button ("Hitung: ",)

if hitung:
    resistance = voltage / current 
    st.success(f"Teganganya adalah {resistance} ohm.")
    st.snow()