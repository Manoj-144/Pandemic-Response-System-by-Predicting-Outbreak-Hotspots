# Global Pandemic Response System

A web-based application designed to predict pandemic outbreak hotspots and support public health decision-making through visual analytics and resource shortage insights across districts in Tamil Nadu using machine learning and synthetic data.

---

## Project Overview

This project aims to:
- Identify potential disease outbreak hotspots using machine learning.
- Visualize the spread and impact of various diseases across districts.
- Analyze contributing environmental, epidemiological, and socioeconomic factors.
- Provide insights into shortages of healthcare resources based on predicted demand.

---

## Methodology

1. **Synthetic Data Simulation**:  
   - Realistic synthetic data was generated for all 30 districts in Tamil Nadu.
   - Data includes cases, R0, temperature, humidity, hospital capacity, ICU beds, ventilators, population metrics, vaccination rates, mobility index, and income-related attributes.

2. **Hotspot Prediction**:  
   - Machine learning models (Random Forest, Gradient Boosting, Decision Trees) were trained to classify districts as potential hotspots.
   - Predictions are based on a combination of disease prevalence and risk factors.

3. **Interactive Analysis Dashboard**:  
   - Plotly-based charts (bar, line, pie, radar, box, scatter, etc.) visualize trends across districts and diseases.
   - Filters allow users to explore data dynamically by selecting disease types and districts.
   - Real-time insights are generated below each chart for easy interpretation.

4. **Resource Shortage Visualization**:  
   - Available medical resources (ICU beds, ventilators, etc.) are predefined in the system.
   - The resource page computes expected demand based on model predictions.
   - It highlights only the **shortages**, giving decision-makers clarity on where additional resources are required.

5. **Geospatial Mapping**:  
   - District-level choropleth maps are created using Tamil Nadu GeoJSON data.
   - Maps display predicted hotspot status and other metadata using color gradients.
   - Implemented using GeoPandas and Folium for accurate and interactive spatial representation.

---

## Key Libraries Used

- **Flask** – Web framework for backend logic
- **Pandas / NumPy** – Data handling and manipulation
- **Scikit-learn** – Machine learning models
- **Plotly** – Interactive data visualizations
- **GeoPandas / Folium** – Map generation and geospatial analysis
- **Select2** – User-friendly dropdown filters for dashboard interaction
- **HTML / CSS / JavaScript / Jinja2** – Frontend and template rendering

---

## Output Highlights

- **District-level Hotspot Prediction**: ML models classify districts by outbreak risk.
- **Data-Driven Charts**: Visual exploration of trends and influencing factors.
- **Interactive Maps**: Districts displayed with color-coded hotspot status.
- **Resource Insights**: Focused view on where shortages exist, based on expected vs predefined available resources.
