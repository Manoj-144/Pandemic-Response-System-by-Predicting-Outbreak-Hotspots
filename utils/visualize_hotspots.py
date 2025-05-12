import pandas as pd
import joblib
import folium
import json
from folium.features import GeoJsonTooltip

# Load your model
model = joblib.load("models\hotspot_model.pkl")

# Load the dataset (should include NAME_2 column)
df = pd.read_csv("data\TN.csv")  # Your latest cleaned & synthetic file

# Group by NAME_2 if needed
# Keep only numeric columns used by the model + 'Taluk'
features = ['Population', 'Density', 'Vaccination Rate', 'Hospital Capacity', 'ICU Beds', 'Mobility Index', 'Cases', 'R0']
df_numeric = df[["Taluk"] + features]

# Group and average
df_grouped = df_numeric.groupby("Taluk").mean().reset_index()


# Load GeoJSON
with open("static\TamilNadu.geojson", "r") as f:
    geojson_data = json.load(f)

# Define features used in model
features = ['Population', 'Density', 'Vaccination Rate', 'Hospital Capacity', 'ICU Beds', 'Mobility Index', 'Cases','R0']

# Make predictions
df_grouped['Hotspot'] = model.predict(df_grouped[features])

# Create a mapping from district name to prediction
hotspot_map = dict(zip(df_grouped['Taluk'], df_grouped['Hotspot']))

# Add the prediction to GeoJSON features
for feature in geojson_data['features']:
    name = feature['properties']['NAME_2']
    feature['properties']['Hotspot'] = hotspot_map.get(name, 0)

# Create folium map centered on Tamil Nadu
m = folium.Map(location=[10.5, 78.5], zoom_start=7, tiles="cartodbpositron")

# Add the GeoJSON as a layer
folium.GeoJson(
    geojson_data,
    name="Hotspot Map",
    style_function=lambda feature: {
        'fillColor': '#e60000' if feature['properties']['Hotspot'] == 1 else '#1a9850',
        'color': 'black',
        'weight': 0.5,
        'fillOpacity': 0.7,
    },
    tooltip=GeoJsonTooltip(fields=['NAME_2', 'Hotspot'], aliases=['District:', 'Hotspot:']),
).add_to(m)

# Add layer control and save
folium.LayerControl().add_to(m)
m.save("tamilnadu_hotspot_map.html")
print("✅ Map saved as tamilnadu_hotspot_map.html")
