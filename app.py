from flask import Flask, render_template, request
import pandas as pd
import joblib
from utils.hotspot_map import generate_all_maps
from utils.resource_allocation import resource_bp
from utils.analysis import get_analysis_charts

app = Flask(__name__)

# Load model and base data
model = joblib.load("models/hotspot_model.pkl")
data = pd.read_csv("data/TN.csv")

@app.route('/')
def home():
    data["Date"] = pd.to_datetime(data["Date"])
    stats = {
        'total_cases': int(data["Cases"].sum()),
        'total_deaths': int(data["Deaths"].sum()),
        'total_recoveries': int(data["Recoveries"].sum()),
        'total_taluks': int(data["Taluk"].nunique())
    }

    trend_df = data.groupby("Date")["Cases"].sum().reset_index().sort_values("Date")
    daily_trend = {
        "dates": trend_df["Date"].dt.strftime("%Y-%m-%d").tolist(),
        "cases": trend_df["Cases"].tolist()
    }

    return render_template("home.html", stats=stats, daily_trend=daily_trend)

@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    diseases = sorted(data["Disease"].unique())
    taluks = sorted(data["Taluk"].unique())

    selected_disease = request.args.get("disease", default="All")
    selected_taluk = request.args.get("taluk", default="All")

    filtered_data = data.copy()
    if selected_disease != "All":
        filtered_data = filtered_data[filtered_data["Disease"] == selected_disease]
    if selected_taluk != "All":
        filtered_data = filtered_data[filtered_data["Taluk"] == selected_taluk]

    charts = get_analysis_charts(filtered_data)

    return render_template("analysis.html", charts=charts,
                           diseases=["All"] + diseases,
                           taluks=["All"] + taluks,
                           selected_disease=selected_disease,
                           selected_taluk=selected_taluk)

@app.route("/hotspots", methods=["GET", "POST"])
def hotspots():
    disease_list = sorted(data["Disease"].dropna().unique())
    selected_disease = request.args.get("disease", None)

    map_html = generate_all_maps(selected_disease)

    return render_template("hotspot.html",
                           disease_list=disease_list,
                           selected_disease=selected_disease,
                           map_html=map_html)

from flask import request, jsonify
from utils.hotspot_map import generate_all_maps, generate_insights

@app.route('/hotspots/data')
def get_hotspot_data():
    disease = request.args.get('disease', '')
    
    # Load data here
    df = pd.read_csv("data/TN.csv")

    filtered_df = df if not disease else df[df['Disease'] == disease]
    
    map_html = generate_all_maps(filtered_df,disease)
    insights = generate_insights(filtered_df)

    return jsonify({
        'map_html': map_html,
        'insights': insights
    })

app.register_blueprint(resource_bp)


if __name__ == "__main__":
    app.run(debug=True)
