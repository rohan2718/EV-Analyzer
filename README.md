# ⚡ EV Analyzer

An interactive dashboard built with **Streamlit**, **Pandas**, and **Altair** that visualizes electric vehicle specifications, performance metrics, and predicts driving range using a machine learning model.

---

## 🚀 Live App  
👉 [Click to View Dashboard](https://ev-analyzer-zhczpvv7v86f2p9vgyv4mo.streamlit.app/)

---

## 📌 Features

### 📊 Brand & Model Insights
- **Top 10 Brands** by number of models
- **Most Efficient EVs** (Wh/km)
- **Segment & Body Type Distribution** with bar charts

### 📈 Performance Visualizations
- Battery Capacity vs Range  
- Efficiency vs Range  
- Torque vs Range

### 🧠 Range Prediction
- User inputs **battery capacity**, **efficiency**, and **torque**
- Predicts **driving range** using a Linear Regression model
- Categorizes results as *Short*, *Mid*, or *High* range

### 📄 Dataset Preview
- Displays first few rows of the loaded datasets

---

## 📁 Dataset Details
The datasets used contain:
- **EV Specifications**: brand, model, battery capacity, efficiency, torque, range, segment, body type
- **Units**: kWh, Wh/km, Nm, km
- Multiple files:
  - `with_Feature.xlsx`
  - `Electric_Data_Updated.xlsx`

---

## 🛠 Tech Stack

| Tool         | Purpose                              |
|--------------|--------------------------------------|
| Python       | Data manipulation & backend logic    |
| Streamlit    | Web app frontend & deployment        |
| Pandas       | Data handling and cleaning           |
| Altair       | Interactive charts                   |
| Matplotlib   | Additional visualizations            |
| Scikit-learn | Machine learning model               |
| Joblib       | Model saving/loading                 |
| Openpyxl     | Excel file support                   |
