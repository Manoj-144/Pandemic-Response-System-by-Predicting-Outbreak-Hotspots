from flask import Blueprint, render_template, request
import pandas as pd

resource_bp = Blueprint('resource_bp', __name__)

# Load your data
df = pd.read_csv('data/TN.csv')  # Adjust path as needed

@resource_bp.route('/resource-allocation')
def resource_allocation():
    disease = request.args.get('disease', '')
    taluk = request.args.get('taluk', '')

    available_resources = {
        'Doctors': 30000,
        'Nurses': 60000,
        'Ambulances': 5000,
        'Medicines': 1000000,
        'Masks': 50000
    }

    filtered_df = df.copy()

    if disease:
        filtered_df = filtered_df[filtered_df['Disease'] == disease]
    if taluk:
        filtered_df = filtered_df[filtered_df['Taluk'] == taluk]

    grouped = filtered_df.groupby(['Taluk', 'Disease']).agg({
        'Cases': 'sum',
        'Hospital Capacity': 'sum',
        'ICU Beds': 'sum',
        'Ventilators': 'sum'
    }).reset_index()

    grouped['Required Doctors'] = (grouped['Cases'] * 0.01).round().astype(int)
    grouped['Required Nurses'] = (grouped['Cases'] * 0.02).round().astype(int)
    grouped['Required Ambulances'] = (grouped['Cases'] * 0.005).round().astype(int)
    grouped['Required Medicines'] = (grouped['Cases'] * 5).round().astype(int)
    grouped['Required Masks'] = (grouped['Cases'] * 2).round().astype(int)

    total_required = {
        'Doctors': grouped['Required Doctors'].sum(),
        'Nurses': grouped['Required Nurses'].sum(),
        'Ambulances': grouped['Required Ambulances'].sum(),
        'Medicines': grouped['Required Medicines'].sum(),
        'Masks': grouped['Required Masks'].sum()
    }

    shortages = {
        key: max(0, total_required[key] - available_resources[key])
        for key in available_resources
    }

    return render_template('resource_allocation.html',
                           grouped_data=grouped.to_dict(orient='records'),
                           shortages=shortages,
                           available=available_resources,
                           disease_list=df['Disease'].dropna().unique(),
                           taluk_list=df['Taluk'].dropna().unique(),
                           selected_disease=disease,
                           selected_taluk=taluk)
