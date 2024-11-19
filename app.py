import streamlit as st
import pandas as pd
import plotly.express as px

# Example Health and Fitness Data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Steps': [5000, 7000, 8000, 9500, 6000, 12000, 13000, 9000, 15000, 11000,
              10000, 9000, 9500, 12000, 8000, 11000, 9500, 10000, 10500, 12000,
              15000, 16000, 14000, 13000, 9000, 9500, 10000, 11500, 12500, 13000],
    'Calories_Burned': [250, 300, 350, 400, 280, 500, 550, 390, 600, 450,
                        420, 380, 410, 500, 350, 460, 420, 440, 460, 510,
                        600, 630, 550, 510, 450, 480, 490, 520, 530, 460]
}


df = pd.DataFrame(data)

print("Lengths of data arrays:")
print("Dates:", len(data['Date']))
print("Steps:", len(data['Steps']))
print("Calories_Burned:", len(data['Calories_Burned']))

# Streamlit Layout
st.title('Health and Fitness Dashboard')

# Dropdown for metric selection
metric = st.selectbox('Select a metric', ['Steps', 'Calories Burned'])

# Filter data based on the selected metric
if metric == 'Steps':
    fig = px.line(df, x='Date', y='Steps', title='Daily Steps')
elif metric == 'Calories Burned':
    fig = px.line(df, x='Date', y='Calories_Burned', title='Calories Burned')

# Display the chart
st.plotly_chart(fig)

# Show basic statistics
st.write(f"Total {metric}: {df[metric].sum()}")
st.write(f"Average {metric}: {df[metric].mean()}")
st.write(f"Maximum {metric}: {df[metric].max()}")
st.write(f"Minimum {metric}: {df[metric].min()}")
