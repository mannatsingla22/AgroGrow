# AgroGrow - Crop Prediction System 🌾

AgroGrow is a machine learning-based system designed to assist farmers and agricultural enthusiasts in identifying the most suitable crop to grow based on soil and environmental conditions. By leveraging data-driven insights, AgroGrow empowers users to make informed decisions, improving productivity and sustainability.

---

## Features 🚀

- **Accurate Crop Recommendations**: Predicts the most suitable crop based on key environmental parameters.
- **Interactive Web Interface**: Dynamically input data via a user-friendly Streamlit website.

---

## Live Demo 🌐

Try AgroGrow online:  
🔗 [https://agrogrow.streamlit.app/](https://agrogrow.streamlit.app/)

---

## Model Comparison and Selection 📊

During the development of AgroGrow, evaluation of three machine learning models was done to determine the best fit for crop prediction based on their accuracy scores:

- **Logistic Regression**: 94.55%
- **Support Vector Machine (SVC)**: 96.14%
- **Random Forest**: **99.32%**

After analyzing the results, **Random Forest** was chosen as the final model for its superior accuracy and ability to handle complex patterns in the data effectively.

---

## Dataset 📊

This project utilizes the **Crop Recommendation Dataset** from Kaggle. The dataset includes the following features:
- **N, P, K**: Soil macronutrients (Nitrogen, Phosphorus, Potassium).
- **Temperature**: Average temperature (°C).
- **Humidity**: Percentage of humidity.
- **pH**: Acidity or alkalinity of the soil.
- **Rainfall**: Annual rainfall (mm).
- **Label**: Crop type.

🔗 [Crop Recommendation Dataset on Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

---

## Technologies Used 🛠️

- **Web App**: Streamlit
- **Libraries**:
  - Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit)

---

## Installation and Usage 📥

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mannatsingla22/AgroGrow.git
   cd AgroGrow
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the web application at:**
   ```
   http://localhost:8501/
   ```