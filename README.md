
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