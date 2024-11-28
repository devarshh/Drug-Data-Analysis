
# Drug Data Analysis 📊💊

Analyzing drug usage data to uncover trends, patterns, and insights that can assist in understanding broader societal and medical implications.

---

## Table of Contents 📂

1. [Introduction](https://github.com/devarshh/drug_data_analysis?tab=readme-ov-file#introduction-)
2. [Objective](#objective)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Technologies Used](#technologies-used)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction 🧠

The **Drug Data Analysis** project dives into comprehensive datasets to explore and understand the factors influencing drug usage, addiction patterns, and their impacts. Through this project, we aim to bridge the gap between data and decision-making in the medical and societal landscape.

---

## Objective 🎯

- Analyze drug usage data for key insights.
- Study patterns to identify high-risk factors.
- Visualize trends for better interpretation.
- Empower researchers and policymakers with actionable data.

---

## Features ✨

- **Data Cleaning**: Comprehensive preprocessing to handle missing or inconsistent data.
- **Exploratory Data Analysis**: Extract key insights and visualize patterns in drug usage.
- **Statistical Analysis**: Advanced techniques to identify correlations and causal relationships.
- **Visualizations**: Interactive and static charts to display findings effectively.

---

## Project Structure 🗂️

```
├── data/
│   ├── raw_data.csv     # Raw dataset
│   ├── processed_data.csv # Cleaned dataset
├── notebooks/
│   ├── EDA.ipynb        # Exploratory Data Analysis notebook
│   ├── Statistical_Analysis.ipynb # Statistical analysis notebook
├── src/
│   ├── cleaning.py      # Data cleaning scripts
│   ├── visualization.py # Visualization functions
├── results/
│   ├── trends.png       # Key trend visualizations
│   ├── correlations.png # Correlation heatmap
├── README.md            # Project documentation
└── requirements.txt     # Dependencies
```

---

## Installation ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/devarshh/drug_data_analysis.git
   cd drug_data_analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage 🖥️

1. Run the data cleaning script:
   ```bash
   python src/cleaning.py
   ```

2. Open Jupyter Notebooks for EDA:
   ```bash
   jupyter notebook notebooks/EDA.ipynb
   ```

3. View results in the `results/` directory for visualizations and insights.

---

## Technologies Used 🛠️

- **Python**: Programming language for data analysis.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib & Seaborn**: Data visualization.
- **Scikit-learn**: Statistical modeling and machine learning.

---

## Contributing 🤝

Contributions are welcome! Follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
