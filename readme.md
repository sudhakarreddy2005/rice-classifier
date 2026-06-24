# 🌾 Rice Classification using PyTorch

## 📌 Overview

This project builds a machine learning model to classify rice types based on physical grain characteristics.
It uses a **PyTorch neural network** and is deployed as an interactive web application using **Streamlit**.

---

## 🚀 Features

* End-to-end ML pipeline (training → saving → inference)
* Custom PyTorch neural network model
* Real-time prediction via Streamlit UI
* Clean and structured project setup
* Ready for deployment

---

## 🧠 Problem Statement

Classify rice grains into categories based on features such as:

* Area
* Major Axis Length
* Minor Axis Length
* Eccentricity
* Convex Area
* Equivalent Diameter
* Extent
* Perimeter
* Roundness
* Aspect Ratio

---

## 🏗️ Model Architecture

A simple feedforward neural network:

* Input Layer → 10 features
* Hidden Layer → 10 neurons
* Output Layer → 1 neuron (binary classification)
* Activation → Sigmoid

---

## 📂 Project Structure

```
rice-classifier/
│
├── model.py          # Model architecture
├── predict.py        # Load model & prediction logic
├── app.py            # Streamlit web app
├── models/
│   └── riceModel.pth  # Trained model weights
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sudhakarreddy2005/rice-classifier.git
cd rice-classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🌐 Live Demo

👉 (Add your Streamlit link here after deployment)

---

## 📊 How It Works

1. User inputs 10 rice grain features
2. Data is passed to the trained PyTorch model
3. Model predicts the rice class
4. Result is displayed instantly in the UI

---

## 🧪 Example Input

```
Area: 15.2
MajorAxisLength: 20.1
MinorAxisLength: 10.5
...
```

---

## 📈 Future Improvements

* Add probability/confidence score
* Improve model with deeper architecture
* Add dataset visualization
* Deploy with FastAPI + React frontend
* Add model explainability (SHAP)

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Streamlit
* NumPy
* Scikit-learn

---

## 🙌 Author

**Sudhakar Reddy**

* GitHub: https://github.com/sudhakarreddy2005

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share!
