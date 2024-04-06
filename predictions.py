import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

def get_total_power_generated():
    wind_power_gen_data = pd.read_csv('csv/final/wind_power_gen_5years.csv')

    X = wind_power_gen_data[['air_temperature', 'pressure', 'wind_speed']]  # Features
    y = wind_power_gen_data['power_generated_by_system']  # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    accuracy = model.score(X_test, y_test)

    validation_data = pd.read_csv('csv/final/wind_power_gen_3months_validation_data.csv')

    X_pred = validation_data[['air_temperature', 'pressure', 'wind_speed']]

    predictions = model.predict(X_pred)

    total_power_generated = sum(predictions)

    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("\nTotal power generated:", total_power_generated)


def use_grid_search():
    wind_power_gen_data = pd.read_csv('csv/final/wind_power_gen_5years.csv')

    X = wind_power_gen_data[['air_temperature', 'pressure', 'wind_speed']]  # Features
    y = wind_power_gen_data['power_generated_by_system']  # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define the parameter grid for Grid Search
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['auto', 'sqrt', 'log2']
    }

    # Create the Random Forest regressor
    rf = RandomForestRegressor(random_state=42)

    # Perform Grid Search with cross-validation
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    grid_search.fit(X_train, y_train)

    # Get the best hyperparameters and model
    best_params = grid_search.best_params_
    best_model = grid_search.best_estimator_

    # Make predictions on the testing set using the best model
    y_pred = best_model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print('Best hyperparameters:', best_params)
    print('Mean Squared Error:', mse)
    print('Mean Absolute Error:', mae)
