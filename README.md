# NetGlobe

NetGlobe is a command-line tool that visualizes the foreign countries your computer is connected to on a 3D globe. It leverages a Python server, an HTTP server, and geolocation data to display your network connections.

## How It Works

1. **Python Server**:
   - Starts a backend server that runs the `netstat -an` command to gather foreign IPs your computer is connected to.
   - Parses the foreign IPs and retrieves the corresponding countries using the IPGeolocation API.

2. **HTTP Server**:
   - Sends requests to the Python server to retrieve processed data about the foreign connections.
   - Serves a 3D globe visualization in your browser.

3. **Visualization**:
   - Opens your browser to display a 3D globe.
   - Shows arcs from your IP location to the countries you're connected to.

## Features

- Visualization of foreign network connections.
- Interactive 3D globe rendered in your browser.
- Uses geolocation API to map IPs to their respective countries.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python3 with module "requests"
- A modern web browser (e.g., Chrome, Firefox, Safari)
- Access to the IPGeolocation API (API key required)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ppazosp/netglobe.git
   cd netglobe
   ```
2. Set up your IPGeolocation API key:
   - Obtain an API key from [IPGeolocation](https://ipgeolocation.io/).
   - Add the key to the python server/netglobe.py file.

3. Run the application:
   ```bash
   ./bin/netglobe
   ```
---

- **Author**: ppazosp
- **GitHub**: [ppazosp](https://github.com/ppazosp)
---

- **Mentions**: [nenadV91](https://github.com/nenadV91/Threejs-globe)

---
