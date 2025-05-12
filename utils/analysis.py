import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

def get_analysis_charts(data: pd.DataFrame):
    charts = {}

    # Ensure Date column is datetime
    if data["Date"].dtype != "datetime64[ns]":
        data["Date"] = pd.to_datetime(data["Date"])

    # 1. Cases Over Time
    cases_time = px.line(data.groupby("Date")["Cases"].sum().reset_index(),
                         x="Date", y="Cases",
                         title="📈 Cases Over Time",
                         markers=True)
    charts["Cases Over Time"] = cases_time.to_html(full_html=False)

    # 2. Deaths Over Time
    deaths_time = px.line(data.groupby("Date")["Deaths"].sum().reset_index(),
                          x="Date", y="Deaths",
                          title="💀 Deaths Over Time",
                          markers=True, line_shape='spline')
    charts["Deaths Over Time"] = deaths_time.to_html(full_html=False)

    # 3. Recoveries Over Time
    recoveries = px.line(data.groupby("Date")["Recoveries"].sum().reset_index(),
                         x="Date", y="Recoveries",
                         title="💚 Recoveries Over Time")
    charts["Recoveries Over Time"] = recoveries.to_html(full_html=False)

    # 4. Cases by Taluk
    taluk_cases = data.groupby("Taluk")["Cases"].sum().sort_values(ascending=False).reset_index()
    taluk_bar = px.bar(taluk_cases, x="Taluk", y="Cases", title="📍 Cases by Taluk",
                       color="Cases", color_continuous_scale="Viridis")
    charts["Cases by Taluk"] = taluk_bar.to_html(full_html=False)

    # 5. Disease-Wise Case Distribution
    disease_dist = px.pie(data.groupby("Disease")["Cases"].sum().reset_index(),
                          names="Disease", values="Cases", title="🦠 Case Distribution by Disease")
    charts["Disease Distribution"] = disease_dist.to_html(full_html=False)

    # 6. R0 (Transmission Rate) Over Time
    r0_chart = px.line(data.groupby("Date")["R0"].mean().reset_index(),
                       x="Date", y="R0", title="🧬 Average R0 Over Time")
    charts["R0 Over Time"] = r0_chart.to_html(full_html=False)

    # 7. Hospital Capacity Usage
    hosp_usage = px.area(data.groupby("Date")[["Hospital Capacity", "ICU Beds", "Ventilators"]].sum().reset_index(),
                         x="Date", y=["Hospital Capacity", "ICU Beds", "Ventilators"],
                         title="🏥 Hospital Resource Availability Over Time")
    charts["Hospital Resources"] = hosp_usage.to_html(full_html=False)

    # 8. Temperature vs Cases (Scatter)
    temp_scatter = px.scatter(data, x="Temperature", y="Cases", color="Disease",
                              title="🌡️ Temperature vs. Cases")
    charts["Temperature vs Cases"] = temp_scatter.to_html(full_html=False)

    # 9. Vaccination Rate vs Cases (Bubble)
    vacc_scatter = px.scatter(data, x="Vaccination Rate", y="Cases",
                              size="Population", color="Taluk",
                              title="💉 Vaccination Rate vs. Cases",
                              size_max=40)
    charts["Vaccination vs Cases"] = vacc_scatter.to_html(full_html=False)

    # 10. Air Quality Impact (Cases vs AQI)
    aqi_chart = px.scatter(data, x="Air Quality Index", y="Cases", color="Taluk",
                           title="🌫️ Air Quality Index vs Cases")
    charts["Air Quality vs Cases"] = aqi_chart.to_html(full_html=False)

    return charts
