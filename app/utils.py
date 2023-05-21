
variables = [
    'A-Alimentary tract and metabolism',
    'A02B-Drugs for peptic ulcer and gastro-oesophageal reflux diseases (GORD)',
    'A10-Drugs used in diabetes',
    'B-Blood and blood forming organs',
    'C-Cardiovascular system',
    'C01A-Cardiac glycosides',
    'C01B-Antiarrhythmics, Class I and III',
    'C02-Antihypertensives',
    'C03-Diuretics',
    'C07-Beta blocking agents',
    'C08-Calcium channel blockers',
    'C09-Agents acting on the Renin-Angiotensin system',
    'C10-Lipid modifying agents',
    'G-Genito urinary system and sex hormones',
    'G03-Sex hormones and modulators of the genital system',
    'H-Systemic hormonal preparations, excluding sex hormones and insulins',
    'J-Antiinfectives for systemic use',
    'J01-Antibacterials for systemic use',
    'M-Musculo-skeletal system',
    'M01A-Antiinflammatory and antirheumatic products non-steroids',
    'N-Nervous system',
    'N02-Analgesics',
    'N05B-Anxiolytics',
    'N05C-Hypnotics and sedatives',
    'N06A-Antidepressants',
    'R-Respiratory system',
    'R03-Drugs for obstructive airway diseases'
]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# # Load the dataset
def predict(variable, country):
    data = pd.read_csv('data/processed.csv')
    plt.figure(dpi=480)

    df = data.loc[(data['Variable'] == variable) & (data['Country'] == country )]
    
    # Prepare the data
    X = df['Year'].values.reshape(-1, 1)
    y = df['Value'].values.reshape(-1, 1)

    # Create polynomial features
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)

    # Fit the polynomial regression model
    model = LinearRegression()
    model.fit(X_poly, y)

    # Predict the sales for next year
    next_year = np.array([[2021]])
    next_year_poly = poly.transform(next_year)
    next_year_sales = model.predict(next_year_poly)[0][0]
    print(f"Predicted sales for next year: {next_year_sales}")

    # Visualize the data and the best fit line
    plt.scatter(X, y, color='blue')
    plt.plot(X, model.predict(X_poly), color='red')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.title('Sales over Time\n'+variable)
    plt.savefig("static/out/predict.png")
    plt.close()

    return round(next_year_sales, 2)
    # plt.show()
    
def get_countrys(variable):
    new_data = pd.read_csv("data/processed.csv")
    cou = {}
    for i in variables:
        df = new_data.loc[new_data['Variable'] == i]
        cou[i] = df['Country'].unique()
    return list(np.sort(cou[variable]))
 