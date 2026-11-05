# DNA-methylation-data-epigenetic-biomarkers
Machine Learning-based analysis and prediction of DNA methylation status using genomic features such as CpG density, genomic location, regulatory scores, and conservation scores. Includes data preprocessing, exploratory data analysis, model development, and performance evaluation.
# DNA Methylation Prediction Using Machine Learning

## Project Overview

This project focuses on predicting DNA methylation status using machine learning classification algorithms. It uses genomic features such as CpG density, genomic location, regulatory score, and conservation score to classify methylation status into two categories (0 and 1).

## Objectives

- Analyze genomic features associated with DNA methylation.
- Perform exploratory analysis of the dataset.
- Develop machine learning classification models.
- Compare model performance using evaluation metrics.
- Identify important features influencing model predictions.
- Optimize model performance through hyperparameter tuning.

## Dataset Description

The dataset contains 1,000 records and five columns.

| Feature | Description |
|---|---|
| cpg_density | CpG site density feature |
| genomic_location | Genomic location-related feature |
| regulatory_score | Regulatory activity-related score |
| conservation_score | Evolutionary conservation-related score |
| methylation_status | Target variable (0 or 1) |

The dataset is divided into:
- Training dataset: 800 records
- Testing dataset: 200 records

*Note: Feature definitions and their biological interpretations require confirmation from the original dataset documentation.*

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## Methodology

1. Dataset Loading and Inspection
2. Exploratory Data Analysis
3. Logistic Regression
4. Decision Tree Classification
5. Random Forest Classification
6. Hyperparameter Tuning using GridSearchCV
7. Model Evaluation and Comparison
8. Feature Importance Analysis
9. Logistic Regression Coefficient Analysis
10. Cross-Validation
11. Model Saving using Joblib

## Model Performance

The following results were obtained on the supplied test dataset:

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 97.5% | 96.49% | 99.10% | 97.78% |
| Decision Tree | 87% | 87.61% | 89.19% | 88.39% |
| Random Forest | 93.5% | 94.55% | 93.69% | 94.12% |
| Tuned Random Forest | 93.5% | 94.55% | 93.69% | 94.12% |

**Best-performing model:** Logistic Regression

Cross-validation accuracy: 97.25% (5-fold).

## Feature Importance

Random Forest feature importance:

1. Regulatory Score – 36.46%
2. CpG Density – 25.78%
3. Genomic Location – 24.04%
4. Conservation Score – 13.72%

## Model Deployment

The trained Logistic Regression model is saved as:

`dna_methylation_model.pkl`

Joblib is used to save and load the trained model.

## How to Run the Project

1. Clone the repository.
2. Install the required libraries:

   `pip install -r requirements.txt`

3. Open Jupyter Notebook:

   `jupyter notebook`

4. Open `DNA_Methylation_Prediction.ipynb`.
5. Execute the notebook cells sequentially.

## Key Findings

- Logistic Regression achieved the highest observed test accuracy of 97.5%.
- Regulatory score had the highest Random Forest feature importance.
- Hyperparameter tuning did not improve Random Forest test performance.
- Logistic Regression achieved an average cross-validation accuracy of 97.25%.

## Limitations

- The dataset contains only 1,000 records.
- The original biological source and feature-generation methodology require verification.
- Model comparisons used the supplied test set, so an independent final evaluation is still recommended.
- Feature importance and model coefficients indicate predictive associations, not biological causation.

## Conclusion

This project demonstrates the application of machine learning techniques to a binary DNA methylation classification problem. Multiple classification algorithms were developed and evaluated, with Logistic Regression achieving the highest observed performance among the models tested.
