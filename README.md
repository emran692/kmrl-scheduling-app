# 🚆 KMRL Train Scheduling Prototype

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)  
[![LightGBM](https://img.shields.io/badge/ML-LightGBM-brightgreen)](https://lightgbm.readthedocs.io/)  
[![OR-Tools](https://img.shields.io/badge/Optimization-Google%20OR--Tools-orange)](https://developers.google.com/optimization)  
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)](https://streamlit.io/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the **Kochi Metro Rail Limited (KMRL) Train Scheduling Prototype**.  
It combines **Machine Learning (LightGBM)** for predictive maintenance risk modeling and **Optimization (Google OR-Tools)** with a **Buffer Period Algorithm** for preventive scheduling.

---

## 📌 Problem Statement
Efficient metro train scheduling is critical to minimize breakdowns, reduce delays, and ensure passenger safety.  
Our solution integrates:
1. **Decision Prediction (ML)** → Predicts whether a train needs **Service / Standby / IBL (Immediate Breakdown Likely)**.  
2. **Optimization Engine** → Allocates trains based on constraints, certificates, mileage, and buffer rules.  

---

## ⚙️ Features
- 📊 **Data Preprocessing & Feature Engineering**
- 🤖 **LightGBM Predictive Model** (`kmrl_risk_model.joblib`)
- 🧩 **Optimization Model with Google OR-Tools**
- ⏱️ **Buffer Period Algorithm** (time & mileage thresholds)
- 📈 **Visualization Dashboard with Streamlit**

---

## ⚡ Installation

### 1. Clone Repository
```bash
git clone https://github.com/emran692/kmrl-scheduling-app.git
cd kmrl-scheduling-app
