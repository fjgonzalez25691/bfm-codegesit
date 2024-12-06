# 🚗 Boltium Fleet Manager (BFM)

Boltium Fleet Manager (BFM) is an innovative fleet management solution designed for VTC (Vehicle for Hire) operators. Built using Atlassian Forge, it integrates seamlessly with Jira and Confluence to simplify and optimize the management of drivers, vehicles, and operational workflows.


## ⚖️ Disclaimer: Ethics and Data Transparency

- **Random Data**: All data used in this project is randomly generated or based on publicly available information. No real or confidential data from any organization has been used.
- **Scripts for Verification**: Data generation scripts are provided in the `scripts/` directory to ensure full transparency in how the data is created.
- **Public Sources**: If public data sources are used, they are clearly cited in the documentation.
- **Commitment to Ethics**: This project adheres to strict ethical standards, avoiding any use of proprietary or sensitive information, and respects the legal and ethical guidelines of all parties involved.

---
## 🌍 Context: A Fictitious Fleet and Platform

For the purpose of this project and the Codegeist 2024 Hackathon, we have created a **fictitious platform** called **Hubify**. Hubify is inspired by existing ride-hailing platforms and serves as the operational framework for our fleet.

### **The Fleet**
- **Name:** Boltium Fleet
- **Fleet Size:** 90 electric vehicles (Zinca 1000 models)
- **Drivers:** 240 highly qualified drivers (with a 10% absence buffer)
- **Vehicles:** The Zinca 1000, a fictitious electric car model inspired by modern EVs.

### **The Platform: Hubify**
Hubify serves as a centralized marketplace for ride-hailing operations. Boltium Fleet Manager connects directly to this platform to:
- Manage driver performance and assignments.
- Monitor vehicle usage and health.
- Generate reports for operational efficiency.

This fictional context allows us to simulate real-world challenges in fleet management while showcasing the power of the Atlassian Forge ecosystem.

## 🌟 Key Features

- **Driver Management**: Centralized database for storing and updating driver details.
- **Vehicle Monitoring**: Comprehensive tracking of vehicle status, assignments, and performance.
- **Operational KPIs**: Monitor key metrics like revenue per hour, customer satisfaction, and absence rates.
- **Integration with Jira**: Assign and manage tasks directly from the app.
- **Integration with Confluence**: Generate automated reports and maintain documentation.

---

## 🛠️ Technology Stack

- **Platform**: [Atlassian Forge](https://developer.atlassian.com/platform/forge/)
- **Backend**: Forge Storage API
- **Frontend**: Custom UI built with Forge modules
- **Data Formats**: JSON for storing drivers and vehicle data
- **Languages**: JavaScript, Python (for data generation)

---

## 📂 Project Structure

```plaintext
enlaces_codegeist/
├── data/                   # JSON files for data
│   ├── drivers.json        # Driver data
│   ├── vehicles.json       # Vehicle data
│   └── zinca1000.json      # Vehicle model specifications
├── scripts/                # Python scripts
│   ├── driver_gen_json.py  # Driver data generation script
│   └── vehicle_gen.py      # Vehicle data generation script
├── .gitignore              # Ignored files and folders (e.g., virtual env, docs)
├── LICENSE                 # License file
├── README.md               # Project overview (this file)
└── doc_conf.md             # Additional documentation (not tracked in git)
```
### Changes in Data Format
To maintain simplicity and ensure compatibility with Atlassian Forge, we decided to standardize all data in JSON format. Scripts and sample JSON files are available in the `data/` and `scripts/` directories.



