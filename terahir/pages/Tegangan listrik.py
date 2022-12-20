import streamlit as st
st.title("hitung Tegangan listrik")


def calculate_voltage(current, resistance):
    # Menghitung tegangan menggunakan rumus V = I * R
    voltage = current * resistance
    return voltage

# Menampilkan form untuk memasukkan nilai arus dan resistansi
current = st.slider("Masukkan nilai arus (dalam ampere):", 0)

resistance = st.number_input("Masukkan nilai resistansi (dalam ohm):", 0)



hitung = st.button ("Hitung: ",)

if hitung:
    voltage = current * resistance    
    st.success(f"Teganganya adalah {voltage}")
    st.snow()