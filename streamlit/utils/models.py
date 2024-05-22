import streamlit as st
import pandas as pd

def models_page():
    st.write("# 💻 Models 💻")
    st.write("Several regression models, including Linear Regression, Ridge Regression, Lasso Regression, Random Forest, Gradient Boosting, and XGBoost, have been defined.\n\n Each model has been instantiated with specific hyperparameters.\n\n")
    st.write("The performance of a model, along with training and test data, was evaluated by the evaluate_model function. The following steps are performed:\n\n")

    st.write("1. A pipeline was created that includes data preprocessing steps  and the regression model.\n\n2. Cross-validation (cross_val_score) was performed on the training data to estimate the model's performance using negative mean squared error as the scoring metric.\n\n",
    "3. The root mean squared error (RMSE) was calculated from the cross-validation scores.\n\n",
    "4. The pipeline was fitted on the entire training data.\n\n",
    "5. The target variable for the test data was predicted.\n\n",
    "6. The mean absolute error (MAE) and root mean squared error (RMSE) for the test predictions were calculated.\n\n",
    "7. A dictionary containing the model's name, cross-validation RMSE mean and standard deviation, test MAE, test RMSE, and the pipeline itself is returned by the function.")

    with st.expander("See code"):
        code = """
# Models to use
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Lasso Regression': Lasso(alpha=0.1),
    'Random Forest': RandomForestRegressor(n_estimators=50, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=50, random_state=42),
    'XGBoost': XGBRegressor(n_estimators=50, random_state=42)
}

# Function to evaluate the models
def evaluate_model(model_name, model, X_train, y_train, X_test, y_test):
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])
    # Cross validation
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
    rmse_scores = (-cv_scores)**0.5
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    return {
        'Model Name': model_name,
        'CV RMSE': rmse_scores.mean(),
        'CV RMSE Std': rmse_scores.std(),
        'Test MAE': mae,
        'Test RMSE': rmse,
        'Pipeline': pipeline
    }

# Evaluation of each model
results = Parallel(n_jobs=-1)(
    delayed(evaluate_model)(name, model, X_train, y_train, X_test, y_test) 
    for name, model in models.items()
)

# Print results
for result in results:
    print(f"Model: {result['Model Name']}")
    print(f"Validation RMSE: {result['CV RMSE']:.2f} ± {result['CV RMSE Std']:.2f}")
    print(f"Test MAE: {result['Test MAE']:.2f}")
    print(f"Test RMSE: {result['Test RMSE']:.2f}")
    print()

# Print the best model
best_model = min(results, key=lambda x: x['Test RMSE'])
        """
        st.code(code, language='python')
    st.write("### 📈 Model Evaluation Results 📈")
    # Results data
    results_data = [
        {
            "Model Name": "Linear Regression",
            "Validation RMSE": 1288.08,
            "Validation RMSE Std": 2.46,
            "Test MAE": 1001.95,
            "Test RMSE": 1293.83
        },
        {
            "Model Name": "Ridge Regression",
            "Validation RMSE": 1288.08,
            "Validation RMSE Std": 2.46,
            "Test MAE": 1001.95,
            "Test RMSE": 1293.83
        },
        {
            "Model Name": "Lasso Regression",
            "Validation RMSE": 1288.08,
            "Validation RMSE Std": 2.46,
            "Test MAE": 1001.95,
            "Test RMSE": 1293.83
        },
        {
            "Model Name": "Random Forest",
            "Validation RMSE": 1383.32,
            "Validation RMSE Std": 1.58,
            "Test MAE": 1050.20,
            "Test RMSE": 1364.94
        },
        {
            "Model Name": "Gradient Boosting",
            "Validation RMSE": 1261.01,
            "Validation RMSE Std": 1.62,
            "Test MAE": 978.84,
            "Test RMSE": 1267.08
        },
        {
            "Model Name": "XGBoost",
            "Validation RMSE": 1259.10,
            "Validation RMSE Std": 1.79,
            "Test MAE": 976.72,
            "Test RMSE": 1265.22
        }
    ]

    # Convert results data to DataFrame
    df_results = pd.DataFrame(results_data)

    # Display the table
    st.table(df_results)
    
    st.write("### 🏆 Best Model 🏆\n\n")
    st.write("")
    st.image("src/images/xgboost.png")
    st.write("#### Reminder:")
    st.write("XGBoost works by combining a number of weak learners to form a strong learner. A weak learner is a machine learning model that is only slightly better than random guessing.\n",
             "However, when weak learners are combined, they can form a strong learner that is much more accurate.\n",
            "XGBoost works by training a number of decision trees. Each tree is trained on a subset of the data, and the predictions from each tree are combined to form the final prediction.\n",
            "XGBoost is an improvement on the GBM algorithm. The main difference is that XGBoost uses a more regularized model, which helps to prevent overfitting."
             )
models_page()
