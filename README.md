<div align="center">
  <img src="./logo.png" alt="ProbeNET Logo" width="150" height="150">
  <br />
  <h1>ProbeNET</h1>
  <p>
    <b>Advanced Domain Intelligence & Security Reconnaissance</b>
  </p>
  <br />

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  </a>
  <a href="https://tailwindcss.com/">
    <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  </a>
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&    logo=open-source-initiative&logoColor=white" alt="License" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Standard-ISO%2FIEC%2027001-red?style=for-the-badge&logo=security-scorecard&logoColor=white" alt="ISO" />
  </a>
</div>

<br />

# About

**ProbeNET** is an advanced domain reconnaissance platform engineered to bridge the gap between raw network data and actionable security insights. It features a highly modular, stateless engine that performs deep-dive analysis on DNS, SSL, and WHOIS layers instantly.

Unlike traditional scanners, ProbeNET operates with a **zero-persistence footprint**, ensuring maximum privacy and speed by processing intelligence in real-time without the overhead of database storage.

# Features

ProbeNET is designed to be lightweight, fast, and compliant with ISO/IEC 25010 software quality models.

- **🌐 Stateless Architecture** - No database required; performs real-time, on-demand lookups.
- **🔍 Deep WHOIS Analysis** - Retrieves registrar details, abuse contacts, and domain age.
- **🛡️ SSL/TLS Inspection** - Validates certificate chains, issuers, and encryption protocols.
- **🗺️ Geo-Location** - Maps the physical location of hosting servers based on IP resolution.
- **🔌 Port Scanning** - Checks availability of critical services (HTTP, SSH, FTP, etc.).
- **🧩 Modular Design** - Easily extensible architecture for adding new scanning modules.

# Getting Started

Follow these steps to set up the development environment.

## Prerequisites
- Python 3.10+
- pip (Python Package Manager)

## Installation

1. **Clone the repository**

        git clone https://github.com/yourusername/ProbeNET.git
        cd ProbeNET

2. **Setup Virtual Environment**

        # Windows:
        python -m venv venv
        venv\Scripts\activate

        # macOS/Linux:
        python3 -m venv venv
        source venv/bin/activate

3. **Install Dependencies**

        pip install -r requirements.txt

4. **Run Server**
   *Note: Since the app is stateless, database migrations are not required.*

        python manage.py runserver

5. **Access the Application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

# Disclaimer

This tool is developed for **educational purposes** and defensive security analysis only. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Please use ProbeNET only on domains you own or have explicit permission to audit.

# License

Distributed under the **MIT License**. See `LICENSE` file for more information.

---

<div align="center">
  <sub>Designed & Developed by Ali Şahin PİŞİRİCİ | 2026</sub>
</div>