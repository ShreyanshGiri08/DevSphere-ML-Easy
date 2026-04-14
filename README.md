# 🟢 Easy: ScoreScouter (The "Burnt-Out" Linear Regressor)
# Challenge Overview 

https://www.kaggle.com/code/vedanthumbe/devsphere-easy-challenge

dataset : https://www.kaggle.com/datasets/peterkmutua/student-hours-scores 

Welcome to ScoreScouter, a predictive engine designed to help students estimate their exam percentages based on their study hours. The previous developer was clearly suffering from "Finals Week Syndrome"—they’ve left you a script that is riddled with simple syntax errors, logical inversions, and data-handling nightmares.

Your mission is to perform a "code rescue." You need to fix the script so it can successfully clean the data, train a Linear Regression model, and visualize the trend line correctly.

This level focuses on fundamental ML workflow: Imports, Data Cleaning, Feature Selection, and Visualization.

# Problem Description 

The ScoreScouter system is contained within a single Google Colab notebook (devsphere_easy_challenge.ipynb) and uses:

- dataset.csv: A simple 2-column dataset containing Hours and Scores.
- scikit-learn: For the Linear Regression engine.
- pandas: For data manipulation.
- matplotlib: For generating the performance graph.

# Real Issues Observed 

When the system was handed over, the following "skill issues" were identified: 

- The Toolbox is Locked: Essential libraries like pandas and sklearn are referenced but never imported.
- Data Disconnect: The dataset path is missing! You need to assign the correct dataset URL to the right variable.
- Invisible Data: A NaN value in the dataset causes the model to crash because the cleaning step wasn't implemented permanently.
- The Mirror World: The model is trying to predict how many hours someone studied based on their score (X and y are swapped).
- Wrong Verb: The model attempts to `train()` which is not a part of standard scikit-learn vocabulary.
- Chart Confusion: A simple line plot is used for plotting individual coordinate data mapping points instead of a scatter plot.
- Visual Hallucinations: The regression line on the graph looks like a scatter plot gone wrong because the prediction logic is feeding the model its own target values.

# Common Bug Types to Look For: 

- Missing Dependencies: Functions being called before their parent libraries are imported.
- Missing References: Variables referencing a path that has not been defined.
- Immutability Errors: Calling a cleaning function (like dropna) without saving the result back to the variable.
- Feature vs. Target Confusion: Misidentifying the independent variable (X) and the dependent variable (y).
- Non-Standard Methods: Specifying model functions that do not map to the library.
- Chart API Confusion: Plotting raw points connected linearly vs. correctly using scatter points.
- Input-Output Mismatch: Passing the wrong variable into the model.predict() function during visualization.

# Your Responsibilities 

- Restore the Environment: Fix the imports so the script recognizes pd and LinearRegression.
- Sanitize the Data: Ensure the null values are actually removed from the DataFrame before training begins.
- Fix the Physics: Correct the X and y assignments. We predict Scores based on Hours, not the other way around.
- Fix the Visuals: Ensure the red regression line accurately represents the model's predictions for the given input hours.

⚠️ Do not modify the student_scores.csv file. All fixes must be made within the code blocks.

# How to Run 

- Open the provided .ipynb file in Google Colab.
- Upload the student_scores.csv to the Colab file storage (or ensure the URL is correct).
- Run the cells sequentially and observe the error messages.
- Apply your fixes until the final output says: ✅ Level 1 Cleared! Your aura is increasing.

# Difficulty Standard 

This is an Entry Level challenge. It is designed to be solved within 10-15 minutes by someone who understands the basic Python ML stack. If you spend more than 5 minutes on the imports, you might need more coffee. 

Good luck, and may your gradients always descend! 
