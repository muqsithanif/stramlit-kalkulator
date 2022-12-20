import streamlit as st
st.title("hitung Arus listrik")

# Menampilkan form untuk memasukkan nilai tegangan dan resistansi
voltage = st.number_input("Masukkan nilai tegangan (dalam volt):", 0)

resistance = st.number_input("Masukkan nilai resistansi (dalam ohm):", 0)



hitung = st.button ("Hitung: ",)

if hitung:
    current = voltage / resistance   
    st.success(f"Teganganya adalah {current} ampere.")
    st.snow()