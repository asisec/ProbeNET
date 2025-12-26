<div align="center">
  <img src="./logo.png" alt="ProbeNET Logo" width="150" height="150">
  <br />
  <h1>ProbeNET</h1>
  <p>
    <b>Advanced Domain Intelligence & Security Reconnaissance</b>
  </p>
  <br />

  <a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</a>

<a href="https://www.djangoproject.com/">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
</a>

<a href="https://tailwindcss.com/">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
</a>

<a href="https://www.docker.com/">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</a>

<a href="https://fastapi.tiangolo.com/">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" />
</a>

<a href="#">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=open-source-initiative&logoColor=white" />
</a>

<a href="#">
  <img src="https://img.shields.io/badge/Standard-ISO%2FIEC%2027001-red?style=for-the-badge&logo=security-scorecard&logoColor=white" />
</a>
</div>

<br />

# About

**ProbeNET** is an advanced domain reconnaissance platform engineered to bridge the gap between raw network data and actionable security insights. It features a highly modular, containerized engine that performs deep-dive analysis on DNS, network, and WHOIS layers instantly.

Unlike traditional scanners, ProbeNET operates with a **zero-persistence footprint**, ensuring maximum privacy and speed by processing intelligence in real-time without the overhead of database storage.

# Features

ProbeNET is designed to be lightweight, fast, and compliant with ISO/IEC 25010 software quality models.

- **🐳 Dockerized Architecture** - Fully containerized services using Docker Compose.
- **🌐 Stateless Architecture** - No database required; performs real-time, on-demand lookups.
- **🔍 Deep WHOIS Analysis** - Retrieves registrar details, abuse contacts, and domain age.
- **📊 Intelligence Scoring** - Automated risk and safety assessment for analyzed domains.
- **🔌 Port Scanning** - Checks availability of critical services (HTTP, SSH, FTP, etc.).
- **🧩 Modular Design** - Easily extensible architecture for adding new scanning modules.

# Getting Started

Follow these steps to set up the environment.

## 🐳 Running with Docker (Recommended)

1. **Clone the repository**

        git clone [https://github.com/asisec/ProbeNET.git](https://github.com/asisec/ProbeNET.git)
        cd ProbeNET

2. **Run with Docker Compose**

        docker-compose up --build

3. **Access the Application**
   - Web UI: `http://localhost:8001`
   - API Docs: `http://localhost:8000/docs`

## 🛠 Manual Installation (Development)

1. **Setup Virtual Environment**

        python -m venv .venv
        # Windows:
        .venv\Scripts\activate
        # macOS/Linux:
        source .venv/bin/activate

2. **Install Dependencies**

        pip install -r requirements.txt

3. **Run Services**

        # Start Scanner
        uvicorn scanner.main:app --port 8000
        # Start Django (New Terminal)
        python manage.py runserver 8001

# Disclaimer

This tool is developed for **educational purposes** and defensive security analysis only. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Please use ProbeNET only on domains you own or have explicit permission to audit.

# License

Distributed under the **MIT License**. See `LICENSE` file for more information.

---

<div align="center">
  <sub>Designed & Developed by Ali Şahin PİŞİRİCİ | 2025</sub>
</div>
