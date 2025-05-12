import pandas as pd
import plotly.express as px
import json

def generate_all_maps(df, selected_disease=None):
    df = pd.read_csv("data/TN.csv")
    geojson_path = "static/TamilNadu.geojson"

    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    if selected_disease:
        df = df[df["Disease"] == selected_disease]

    latest_date = df["Date"].max()
    latest_df = df[df["Date"] == latest_date]

    grouped = latest_df.groupby("Taluk")["Cases"].sum().reset_index()
    grouped.columns = ["Taluk", "Cases"]

    fig = px.choropleth(
        grouped,
        geojson=geojson_data,
        locations="Taluk",
        featureidkey="properties.NAME_2",
        color="Cases",
        color_continuous_scale="Reds",
        title=f"Disease Outbreak Hotspots - {selected_disease if selected_disease else 'All Diseases'}",
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0}, height=500)

    return fig.to_html(full_html=False)

def generate_insights(df):
    return [
        {"title": "Total Cases", "value": int(df["Cases"].sum())},
        {"title": "Total Deaths", "value": int(df["Deaths"].sum())},
        {"title": "Avg. Reproduction Number (R0)", "value": round(df["R0"].mean(), 2)},
    ]

