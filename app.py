
import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="DNA Methylation Prediction",
    page_icon="🧬",
    layout="wide"
)

# Load model
model = joblib.load("dna_methylation_model.pkl")

# Custom CSS
st.markdown("""
<style>
.title {
    text-align: center;
    color: #60A5FA;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #CBD5E1;
    font-size: 17px;
}

h2, h3 {
    color: #60A5FA;
}
</style>
""", unsafe_allow_html=True)


# HEADER
st.markdown(
    '<p class="title">🧬 DNA Methylation Prediction</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning-Based Genomic Classification</p>',
    unsafe_allow_html=True
)

st.divider()


# PROJECT OVERVIEW
st.subheader("Project Overview")

st.write(
    "This application uses a trained Logistic Regression model "
    "to predict methylation status based on four genomic features."
)

st.info(
    "Enter feature values between 0 and 1 to generate a prediction."
)

st.divider()


# INPUT SECTION
st.subheader("Genomic Feature Inputs")

col1, col2 = st.columns(2)

with col1:
    cpg_density = st.slider(
        "CpG Density", 0.0, 1.0, 0.5
    )

    regulatory_score = st.slider(
        "Regulatory Score", 0.0, 1.0, 0.5
    )

with col2:
    genomic_location = st.slider(
        "Genomic Location", 0.0, 1.0, 0.5
    )

    conservation_score = st.slider(
        "Conservation Score", 0.0, 1.0, 0.5
    )

st.divider()


# PREDICTION
if st.button("Predict Methylation Status", use_container_width=True):

    input_data = pd.DataFrame([{
        "cpg_density": cpg_density,
        "genomic_location": genomic_location,
        "regulatory_score": regulatory_score,
        "conservation_score": conservation_score
    }])

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    st.subheader("Prediction Results")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.metric(
            "Predicted Status",
            str(prediction)
        )

    with result_col2:
        st.metric(
            "Prediction Confidence",
            f"{max(probabilities) * 100:.2f}%"
        )

    st.write("### Class Probabilities")

    st.write("Class 0")
    st.progress(float(probabilities[0]))

    st.write("Class 1")
    st.progress(float(probabilities[1]))

    st.caption(
        "Probabilities are model estimates, not experimentally "
        "validated biological measurements."
    )


# FOOTER
st.divider()

st.caption(
    "DNA Methylation Prediction | Machine Learning Project"
)
