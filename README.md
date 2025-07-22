# Winning the Space Race with Data Science

## Capstone Project – Coursera IBM Data Science Certificate  
**Author:** Bryan Edward Villon  
**Project Goal:** Predict Falcon 9 first-stage landing outcomes using historical data and machine learning

---

## Overview

This project explores how SpaceX revolutionized space launch economics by reusing Falcon 9 first stages. By predicting landing outcomes, competitors and stakeholders can assess mission risks and launch costs more accurately.

A complete end-to-end data science pipeline was built using:

- API data collection
- Web scraping
- Data wrangling and transformation
- Exploratory data analysis (EDA)
- SQL-based analysis
- Interactive visualizations with Folium and Plotly Dash
- Predictive modeling using classification algorithms

---

## Repository Structure

| Module | Description | Notebook |
|--------|-------------|----------|
| Module 1 | Data Collection | [`1_1-jupyter-labs-spacex-data-collection-api.ipynb`](./1_1-jupyter-labs-spacex-data-collection-api.ipynb) |
| Module 1 | Web Scraping | [`1_2-jupyter-labs-webscraping.ipynb`](./1_2-jupyter-labs-webscraping.ipynb) |
| Module 1 | Data Wrangling | [`1_3-labs-jupyter-spacex-Data wrangling.ipynb`](./1_3-labs-jupyter-spacex-Data%20wrangling.ipynb) |
| Module 2 | EDA with SQL | [`2_1-jupyter-labs-eda-sql-coursera_sqllite.ipynb`](./2_1-jupyter-labs-eda-sql-coursera_sqllite.ipynb) |
| Module 2 | EDA with Visualization | [`2_2-edadataviz.ipynb`](./2_2-edadataviz.ipynb) |
| Module 3 | Interactive Map | [`3_1_lab-jupyter-launch-site-location-v2.ipynb`](./3_1_lab-jupyter-launch-site-location-v2.ipynb) |
| Module 3 | Plotly Dash Dashboard | [`3_2-spacex-dash-app.py`](./3_2-spacex-dash-app.py) |
| Module 4 | ML Pipeline & Prediction | [`4_1-SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb`](./4_1-SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb) |

---

## Dashboard Preview

- Plotly Dash App: Interactive charts for site-level launch success, payload correlation, and filter controls  
- Folium Map: Geographical visualization of launch sites and landing outcomes  

---

## ML Model Highlights

- Classification models tested: Logistic Regression, SVM, Decision Tree, KNN  
- All models achieved ~83.3% accuracy  
- High precision on predicting successful landings (no false negatives)

---

## Conclusion

The project demonstrates how data science can provide actionable insights in aerospace economics and operations. Falcon 9 landing success can be reliably predicted using public launch data and machine learning techniques.

---

## License

This project is submitted as part of the **Coursera IBM Data Science Capstone** and is publicly available for educational and peer-review purposes.

