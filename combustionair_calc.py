
# Combustion air calculator for Brad Smith
# Brittany Smith
# 9/26/2025

import os
import sys
import webview

def calculate_combustion_air(appliance_btu_input):
    volume_per_1000_btu = 50 # in cubic feet
    opening_outdoor = 4000   # BTU/hr per 1 in^2
    opening_indoor = 1000    # BTU/hr per 1 in^2

    required_volume = (appliance_btu_input / 1000) * volume_per_1000_btu
    opening_area_outdoor_each = appliance_btu_input / opening_outdoor
    opening_area_indoor_each = appliance_btu_input / opening_indoor

    return {
        "Required Room Volume (ft³)": round(required_volume, 2),
        "Outdoor Opening Size per opening (in²)": round(opening_area_outdoor_each, 2),
        "Indoor Opening Size per opening (in²)": round(opening_area_indoor_each, 2)
    }

class Api:
    def calculate(self, btu):
        try:
            btu = float(btu)
            results = calculate_combustion_air(btu)
            html = "<ul>"
            for key, value in results.items():
                html += f"<li><b>{key}:</b> {value}</li>"
            html += "</ul>"
            return html
        except ValueError:
            return "<span style='color:red;'>❌ Please enter a valid number.</span>"
        
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller adds a _MEIPASS attribute when running as an executable
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# Load HTML from file
with open(resource_path("index.html"), "r", encoding="utf-8") as f:
    html = f.read()


if __name__ == '__main__':
    api = Api()
    webview.create_window('Combustion Air Calculator', html=html, js_api=api, width=500, height=400)
    webview.start()