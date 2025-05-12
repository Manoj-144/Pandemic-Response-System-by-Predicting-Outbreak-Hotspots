# Pandemic Response System – Tamil Nadu, India

A web-based application focused on predicting pandemic outbreak hotspots and analyzing healthcare resource shortages across districts of Tamil Nadu using synthetic data and machine learning techniques.

---

## Project Overview

This project is designed to:
- Identify high-risk districts for disease outbreaks.
- Visualize disease trends and contributing factors across Tamil Nadu.
- Provide insights into shortages of healthcare resources based on predicted demand.

---

## Methodology

1. **Synthetic Data Generation**  
   - Realistic synthetic datasets were created for all 30 districts of Tamil Nadu.  
   - Data includes epidemiological (cases, recoveries, deaths, R0), environmental (temperature, humidity, rainfall), healthcare (hospital capacity, ICU beds, ventilators), and socioeconomic variables (population, income, poverty rate, mobility index).

2. **Hotspot Prediction**  
   - Machine learning models such as Random Forest, Gradient Boosting, and Decision Trees are trained to predict whether a district is a potential hotspot.  
   - Models use a combination of health, environmental, and mobility indicators.

3. **Interactive Data Analysis Dashboard**  
   - Users can explore disease trends and patterns using multi-select filters for disease and district.  
   - Visualizations include bar, line, pie, radar, scatter, box, and area charts created using Plotly.  
   - Each chart is accompanied by real-time dynamic insights based on the filtered data.

4. **Resource Shortage Visualization**  
   - Predefined available resources (ICU beds, ventilators, etc.) are stored in the system.  
   - Based on predicted case loads, the system estimates required resources per district.  
   - The resource page displays **only the shortages**, helping authorities prioritize allocation.

5. **Geospatial Mapping**  
   - District-wise hotspot predictions are visualized using choropleth maps.  
   - Maps are generated using Tamil Nadu GeoJSON files and rendered with GeoPandas and Folium.  
   - Color gradients indicate hotspot intensity or resource scarcity.

---

## Libraries & Technologies Used

- **Flask** – Backend web framework  
- **Pandas / NumPy** – Data processing and analysis  
- **Scikit-learn** – Machine learning models  
- **Plotly** – Interactive charts and visualizations  
- **GeoPandas / Folium** – Map rendering and geospatial analysis  
- **HTML / CSS / JavaScript / Jinja2** – Frontend development  
- **Select2** – Enhanced multi-select dropdowns for filters

---

## Key Features

- **District-Level Hotspot Prediction**: Real-time classification of outbreak-prone areas.  
- **Dynamic Data Exploration**: Multi-filter dashboards with insights across multiple dimensions.  
- **Choropleth Maps**: Visual representation of disease severity and hotspot density across Tamil Nadu.  
- **Resource Shortage Highlights**: Focus on districts that may require more medical support based on predefined availability and predicted needs.
