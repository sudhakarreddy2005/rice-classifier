import streamlit as st
from predict import predict

st.title("🌾 Rice Classifier")

Area = st.number_input("Area")
MajorAxisLength = st.number_input("Major Axis Length")
MinorAxisLength = st.number_input("Minor Axis Length")
Eccentricity = st.number_input("Eccentricity")
ConvexArea = st.number_input("Convex Area")
EquivDiameter = st.number_input("Equivalent Diameter")
Extent = st.number_input("Extent")
Perimeter = st.number_input("Perimeter")
Roundness = st.number_input("Roundness")
AspectRation = st.number_input("Aspect Ratio")

if st.button("Predict"):
    data = [
        Area,
        MajorAxisLength,
        MinorAxisLength,
        Eccentricity,
        ConvexArea,
        EquivDiameter,
        Extent,
        Perimeter,
        Roundness,
        AspectRation
    ]

    result = predict(data)
    if result == 0:
        st.success("Rice Type: Type GENEN")
    else:
        st.success("Rice Type: Type SHINH")
    