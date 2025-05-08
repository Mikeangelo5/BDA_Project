# BDA Project

## Project Overview
This project investigates educational disparities in access to essential services such as healthcare, education, and commercial centers. It uses supervised machine learning techniques to analyze whether households led by individuals with lower educational attainment face longer distances to essential services.

## Key Features
- Data exploration and preprocessing
- Linear regression and Random Forest models for prediction
- Classification models to categorize distance into short, medium, or long
- Cross-validation and performance evaluation

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mikeangelo5/BDA_Project.git


2. **Install dependencies**:
Ensure you have Python 3.x installed. Then, install the necessary libraries:

bash
Copy
pip install -r requirements.txt
3. **Run the project**:

The main script is located in main.py. To run it, execute:

bash
Copy
python main.py
Data
The dataset used in this project is publicly available from Eesti Statistical Database.

**Methodology**
This project applies Supervised Machine Learning techniques:

Regression Models: Linear regression and Random Forest Regression

Classification Models: Logistic Regression, Decision Trees, and Random Forest Classifiers

Evaluation: The models are evaluated using metrics like R², accuracy, precision, recall, and F1-score.

Challenges and Solutions
Expected Challenges:
Limited Feature Set: The dataset mainly contains education level and distance data, limiting model complexity.

Data Imbalance: Some education levels may have fewer entries, which could affect the model’s accuracy.

Solutions:
Apply techniques like oversampling and feature engineering to mitigate these issues.

**Contributors**
Yagub Hajiyev

Elchin Huseynov
