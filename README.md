# Evaluating the Diagnostic Power of the Gut Microbiome in IBD using Explainable Machine Learning

## Overview

This project investigates whether gut microbiome data can be used to distinguish patients with Inflammatory Bowel Disease (IBD) from healthy individuals. Using microbiome profiles from the iHMP IBD Multi-omics Database, we developed and evaluated machine learning models for the classification of:

* Crohn's Disease (CD) vs Healthy Controls
* Ulcerative Colitis (UC) vs Healthy Controls

The workflow includes data preprocessing, feature selection, model training, explainable AI techniques, and fairness analysis to identify reliable microbial biomarkers associated with IBD.

## What We Did

* Processed gut microbiome abundance data using filtering, normalization, and CLR transformation.
* Compared multiple machine learning models, including Logistic Regression, SVM, Random Forest, and XGBoost.
* Applied feature selection techniques such as PCA and Kruskal-Wallis filtering.
* Used Explainable AI (SHAP values and model coefficients) to identify important microbial biomarkers.
* Investigated disease-specific microbial signatures for Crohn's Disease and Ulcerative Colitis.
* Evaluated the impact of demographic metadata (age and gender).
* Performed fairness and confounding-factor analyses to verify that predictions were driven by disease-related biological signals rather than demographic biases.

## Contributors

* Dimitrios Kampanakis
* Reinti Pasai
* Charalampos Spyropoulos
* Grigorios-Panagiotis Papandrikopoulos
