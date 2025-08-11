import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("with Feature.xlsx")

# Title
st.title("🔋 EV Range Predictor Dashboard")


# Set page config
# st.set_page_config(page_title="EV Analyzer", layout="wide")

# Title
# st.title("🔋 Electric Vehicle Analyzer Dashboard")
st.subheader("📊 Top 10 Brands with the Most Number of Models")

# Load data
# df = pd.read_excel("Data/Electric_Data_Updated.xlsx")

# Prepare data
brand_count = df['brand'].value_counts().head(10)

# Convert to DataFrame (required format for st.bar_chart)
brand_df = pd.DataFrame({
    'Brand': brand_count.index,
    'Number of Models': brand_count.values
}).set_index("Brand")

# Show bar chart in Streamlit
st.bar_chart(brand_df)


st.set_page_config(page_title="EV Analyzer", layout="wide")

# Title
# st.title("🔋 Electric Vehicle Analyzer Dashboard")
st.subheader("🌿 Top 10 Most Efficient Electric Vehicles (Wh/km)")

# Load data
# df = pd.read_excel("Data/Electric_Data_Updated.xlsx")

# Prepare data
efficient_models = df[['brand', 'model', 'efficiency_wh_per_km']].dropna()
efficient_models = efficient_models.sort_values(by='efficiency_wh_per_km').head(10)
efficient_models['Full Name'] = efficient_models['brand'] + ' ' + efficient_models['model']

# Format for st.bar_chart
efficiency_df = efficient_models[['Full Name', 'efficiency_wh_per_km']].set_index('Full Name')

# Show bar chart
st.bar_chart(efficiency_df)


import altair as alt

st.set_page_config(page_title="EV Analyzer", layout="wide")

# Title
# st.title("🔋 Electric Vehicle Analyzer Dashboard")
st.subheader("🚗 EV Segment Distribution")

# Load data
# df = pd.read_excel("Data/Electric_Data_Updated.xlsx")


# Prepare and sort data
segment_counts = df['segment'].value_counts().dropna()
segment_df = pd.DataFrame({
    'EV Segment': segment_counts.index,
    'Number of Models': segment_counts.values
}).sort_values(by='Number of Models', ascending=False)

# Altair bar chart
chart = alt.Chart(segment_df).mark_bar().encode(
    x=alt.X('EV Segment', sort='-y'),
    y='Number of Models'
).properties(
    width=700,
    height=400,
    title='EV Segment Distribution'
)

# Show chart in Streamlit
st.altair_chart(chart, use_container_width=True)


st.subheader("🚘 EV Body Type Distribution")

# Load data
# df = pd.read_excel("Data/Electric_Data_Updated.xlsx")

# Count car body types
body_type_counts = df['car_body_type'].value_counts().dropna()
body_type_df = pd.DataFrame({
    'Car Body Type': body_type_counts.index,
    'Number of Models': body_type_counts.values
}).sort_values(by='Number of Models', ascending=False)

# Altair bar chart
chart = alt.Chart(body_type_df).mark_bar().encode(
    x=alt.X('Car Body Type', sort='-y'),
    y='Number of Models'
).properties(
    width=700,
    height=400,
    title='Electric Vehicle Body Type Distribution'
)

# Show chart
st.altair_chart(chart, use_container_width=True)

# Select features and target
features = ['battery_capacity_kWh', 'efficiency_wh_per_km', 'torque_nm']  # adjust if different
target = 'range_km'

X = df[features]
y = df[target]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'ev_range_predictor.pkl')

# Sidebar for user input
st.sidebar.header("📥 Enter EV Specs")
battery = st.sidebar.number_input("Battery Capacity (kWh)", min_value=0.0, value=50.0)
efficiency = st.sidebar.number_input("Efficiency (Wh/km)", min_value=100.0, value=160.0)
torque = st.sidebar.number_input("Torque (Nm)", min_value=100.0, value=300.0)

st.subheader("🚘 EV Range Analyzer Result")

# Predict
input_data = pd.DataFrame([[battery, efficiency, torque]], columns=features)
predicted_range = model.predict(input_data)[0]

# Determine badge styling
if predicted_range < 150:
    emoji = "🟥"
    label = "Short Range"
    gradient = "linear-gradient(135deg, #ff4e50, #f9d423)"  # Red-Orange
elif 150 <= predicted_range < 300:
    emoji = "🟨"
    label = "Mid Range"
    gradient = "linear-gradient(135deg, #fbd786, #f7797d)"  # Yellow-Peach
else:
    emoji = "🟩"
    label = "High Range"
    gradient = "linear-gradient(135deg, #56ab2f, #a8e063)"  # Green-Lime

# st.info(f"Category: {category}")
# Render stylish badge
st.markdown(f"""
<div style="
    background: {gradient};
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    font-family: 'Segoe UI', sans-serif;
    margin-bottom: 20px;
">
    <h1 style="color: white; font-size: 48px; margin: 0;">{emoji} {label}</h1>
    <p style="font-size: 22px; color: white; margin-top: 10px;">
        🚗 Estimated Range: <strong style="font-size: 28px;">{predicted_range:.2f} KM</strong>
    </p>
</div>
""", unsafe_allow_html=True)
# Display prediction and category
# st.success(f"Estimated Range: {predicted_range:.2f} km")
# st.info(f"Category: {category}")

st.set_page_config(page_title="EV Analyzer", layout="wide")

# Subheader
st.subheader("📈 Data Insights")

# Load data
# df = pd.read_excel("Data/Electric_Data_Updated.xlsx")

# Define features and target
features = ['battery_capacity_kWh', 'efficiency_wh_per_km', 'torque_nm']
target = 'range_km'

# Prepare individual scatter plots
chart1 = alt.Chart(df).mark_circle(color='teal', size=60).encode(
    x='battery_capacity_kWh',
    y='range_km'
).properties(
    title='Battery Capacity vs Range',
    width=300,
    height=300
)

chart2 = alt.Chart(df).mark_circle(color='orange', size=60).encode(
    x='efficiency_wh_per_km',
    y='range_km'
).properties(
    title='Efficiency vs Range',
    width=300,
    height=300
)

chart3 = alt.Chart(df).mark_circle(color='purple', size=60).encode(
    x='torque_nm',
    y='range_km'
).properties(
    title='Torque vs Range',
    width=300,
    height=300
)

# Combine charts side by side
combined_chart = alt.hconcat(chart1, chart2, chart3).configure_axis(
    grid=True
)

# Display in Streamlit
st.altair_chart(combined_chart, use_container_width=True)

# Display the data
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())




