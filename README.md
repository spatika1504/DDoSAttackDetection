
# DDoSAttackDetection
To classify between DDoS Attacks and Benign traffic

# DDoS Detection and Model Serving

## Overview

This repository contains a complete solution for detecting DDoS attacks using machine learning. The project includes:

- **Data Preprocessing & EDA:** Jupyter Notebook for cleaning the data, performing exploratory analysis, and feature engineering.
- **Model Training & Evaluation:** In the Notebook I train multiple classifiers, evaluate their performance, and select the best model.
- **Model Serving:** A Flask API (`app.py`) that loads the best model (`best_model.pkl`) and exposes a `/predict` endpoint for real-time predictions.


## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/spatika1504/DDoSAttackDetection.git
   cd DDoSAttackDetection

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Running the Notebooks**

    Open the notebook **DuneSecurityML.ipynb** in Jupyter Notebook or Jupyter Lab and run the cells. 

4. **Running the Flask API:**

    In the terminal run 
    ```bash
    python app.py
    ```
    
    Flask API will start at http://127.0.0.1:5000

    We can then Test the prediction endpoint by sending a POST request to http://127.0.0.1:5000/predict with JSON data.

