import streamlit as st

st.set_page_config(
    page_title='multipage app',
    page_icon='M'
)

st.title("Hitung rangkaian pararel")

    # Get input values for individual resistances
R1 = st.number_input("Masukkan nilai hambatan R1", 0)
R2 = st.number_input("Masukkan nilai hambatan R2", 0)
R3 = st.number_input("Masukkan nilai hambatan R3", 0)

    # Calculate total resistance when the "Hitung" button is clicked
hitung = st.button("Hitung")
if hitung:
        # Calculate total resistance using the formula above
        Rt = 1/(1/R1 + 1/R2 + 1/R3)
        st.success(f"Hambatannya adalah {Rt}")
        st.snow()