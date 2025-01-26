#!/opt/homebrew/Cellar/netglobe/1.0.0/netglobe_env/bin/python

import requests
import subprocess
import re
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api_key = ""

def get_my_ip_country():
    try:
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            my_ip = data.get("ip")
            my_country = data.get("country_name", "Unknown")
            return my_country
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error fetching my IP and country: {e}")
        return "Unknown"

def get_foreign_ips():
    try:
        result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        foreign_ips = []
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        for line in lines:
            parts = line.split()
            if len(parts) >= 5 and re.match(ip_pattern, parts[4]):
                ip = parts[4].rsplit('.', 1)[0]  
                foreign_ips.append(ip)
        return list(set(foreign_ips))  

        print(f"Error executing netstat: {e}")
        return []
    except Exception as e:
        print(f"Error fetching my country for my IP: {e}")
        return "Country not found"

def get_country(ip):
    try:
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("country_name", "Unknown")
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error fetching country for IP {ip}: {e}")
        return "Country not found"

def build_connections():
    my_country = get_my_ip_country()
    connections = {my_country: []}
    for ip in get_foreign_ips():
        country = get_country(ip)
        if country != "Unknown" and country != my_country:
            connections[my_country].append(country)
    connections[my_country] = list(set(connections[my_country])) 
    return connections

@app.route("/connections", methods=["GET"])
def serve_connections():
    try:
        connections = build_connections()
        return jsonify(connections)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, port=8000)
