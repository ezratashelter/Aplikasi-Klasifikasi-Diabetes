import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Judul aplikasi
st.title("Prediksi Diabetes dengan SVM")

# Deskripsi aplikasi
st.write("Masukkan data kesehatan Anda untuk mengetahui risiko diabetes.")

# Input data dari user
col1, col2 = st.columns(2)

with col1 :
    pregnancies = st.number_input("Jumlah Kehamilan", min_value=0, max_value=20)
with col2 :
    glucose = st.number_input("Glukosa", min_value=0, max_value=200,)
with col1 :
    blood_pressure = st.number_input("Tekanan Darah", min_value=0, max_value=150)
with col2 :
    skin_thickness = st.number_input("Ketebalan Kulit", min_value=0, max_value=100)
with col1 :
    insulin = st.number_input("Insulin", min_value=0, max_value=900)
with col2 :
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0)
with col1 :
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5)
with col2 :
    age = st.number_input("Usia", min_value=0, max_value=120)

# Load model
def load_model():
    with open("svm_model.pkl", "rb") as f:
        model, scaler = pickle.load(f)
    return model, scaler

# Prediksi
if st.button("Prediksi"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error(f"Prediksi: **Pasien Terkena Diabetes**")
    else:
        st.success(f"Prediksi: **Pasien Tidak Diabetes**")
