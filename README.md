
# Sustanibility
  So far we have converted data set into a data frame to visualise the data set. Now we are working on the next step of cleaning, preprocessing and feature engineeirng.

### At 5pm
  - We implmeted some merging functionality on grid data, set which basically merges all the seperate five years of data into one csv file.

  - This enabales us to efficiently preprocessed the data for future uses.

  - Now next step is to pre-proccess the merged grid data and remove duplicacy and nullability.

### At 7pm 
  - We pre-processed the merged grid data and removed duplicate and null values (in our case thier our none).

  - We also generated correlation between c1, c2, c3, p1, p2, p3 columns to visualized the threshold.

  - We then performed feature engineering on the grid data where we encoded the stability column to have numerical values to better understanding for the model.

  - Then we scaled all the numerical columns as it leads to better model performance and avoid numerical instabilities.

### At 1am
  - we coverted the all 20 excel files that contains five years of wind power data into csv files and merged them into the final wind power data.

  - Then using that final input data and the provided 3 months validation dataset, we predicted the total power generated (p) value for the first 3 months of 2024.

  - Now, we implemented the first part of the problem statement and figuring out what to do for the next part of the problem statement.


### Instructions to run the code:
- First clone the repo
    ```
    git clone https://github.com/HARDIKSANKHE/17_sustainabilityandenvironment_WebPixels.git
    ```

- In terminal, Go to cloned folder and install the dependencies
    ```
    cd 17_sustainabilityandenvironment_WebPixels
    pip install -r requirements.txt
    ```

- Run main.py to get predictions
    
    #in windows
    ```
    python main.py   
    ```

    #in linux and macOs
    ```
    python3 main.py
    ```
                