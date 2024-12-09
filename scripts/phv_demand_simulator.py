# Script to generate synthetic hourly PHV demand for a one-week period with error handling.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_synthetic_phv_demand(start_date='2024-12-09', end_date='2024-12-15', output_filename='synthetic_phv_demand.csv'):
    """
    Generates a synthetic dataset representing the hourly demand for Private Hire Vehicles (PHV) over a one-week period.
    
    Parameters:
    - start_date (str): The start date for the dataset in the format 'YYYY-MM-DD'.
    - end_date (str): The end date for the dataset in the format 'YYYY-MM-DD'.
    - output_filename (str): The name of the CSV file to save the generated data.
    
    Returns:
    - DataFrame: A Pandas DataFrame containing the synthetic PHV demand data.
    """
    try:
        # Set random seed for reproducibility
        np.random.seed(42)
        
        # Step 1: Generate a range of hourly timestamps between start_date and end_date
        print("Generating date range from", start_date, "to", end_date)
        fechas = pd.date_range(start=start_date, end=end_date, freq='H')

        # Check if the date range is valid
        if fechas.empty:
            raise ValueError("The date range is empty. Please check your start_date and end_date.")

        # Step 2: Initialize an empty list to store demand for each hourly slot
        demand = []

        # Step 3: Define demand patterns for weekdays and weekends
        for fecha in fechas:
            hour = fecha.hour
            day_of_week = fecha.dayofweek  # 0 = Monday, 6 = Sunday

            # Define base demand according to the hour and day of the week
            if day_of_week < 5:  # Weekdays (Monday to Friday)
                if 7 <= hour < 9 or 17 <= hour < 19:
                    base_demand = 80  # Peak hours
                else:
                    base_demand = 30  # Non-peak hours
            else:  # Weekends (Saturday and Sunday)
                if 20 <= hour or hour < 2:  # Night hours (Party time)
                    base_demand = 70  # Peak demand at night on weekends
                else:
                    base_demand = 40  # Lower demand during the day
           
            # Add randomness to simulate fluctuations
            demand_hour = np.random.poisson(lam=base_demand)
            demand.append(demand_hour)

        # Step 4: Create a DataFrame to store the demand data
        print("Creating DataFrame with demand data.")
        df = pd.DataFrame({'datetime': fechas, 'demand': demand})

        # Extract 'hour' and 'day of week' to prepare data for heatmap
        df['hour'] = df['datetime'].dt.hour
        df['day_of_week'] = df['datetime'].dt.dayofweek  # 0 = Monday, 6 = Sunday

        # Step 5: Validate the DataFrame
        if df.empty:
            raise ValueError("The DataFrame is empty. Please review the data generation logic.")

        # Step 6: Export the DataFrame to a CSV file
        print("Saving the DataFrame to CSV file:", output_filename)
        df.to_csv(output_filename, index=False)

        # Check if the file was created successfully
        if not os.path.isfile(output_filename):
            raise IOError(f"File '{output_filename}' could not be created.")

        print("Data successfully saved to", output_filename)

        # Step 7: Generate a heatmap to visualize demand distribution
        print("Creating heatmap to visualize hourly demand distribution by day of the week.")
        
        # Group by day of the week and hour, summing up the total demand
        demand_by_day_hour = df.groupby(['day_of_week', 'hour'])['demand'].sum().reset_index()
        
        # Calculate the total daily demand to normalize the hourly percentage
        total_demand_by_day = df.groupby('day_of_week')['demand'].sum().reset_index()
        
        # Merge the total demand for normalization
        demand_by_day_hour = demand_by_day_hour.merge(total_demand_by_day, on='day_of_week', suffixes=('', '_total'))
        demand_by_day_hour['percentage'] = (demand_by_day_hour['demand'] / demand_by_day_hour['demand_total']) * 100

       # Pivot the data to create a matrix for the heatmap
        heatmap_data = demand_by_day_hour.pivot(index='day_of_week', columns='hour', values='percentage')

        # Plot the heatmap
        plt.figure(figsize=(12, 6))
        sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt=".1f", cbar=True)
        plt.title('PHV Demand Distribution by Hour and Day of the Week (%)')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Day of the Week (0 = Monday, 6 = Sunday)')
        plt.show()
        
        return df

    except ValueError as ve:
        print("ValueError:", ve)
    except IOError as ioe:
        print("IOError:", ioe)
    except Exception as e:
        print("An unexpected error occurred:", e)


# Run the function to generate and save the synthetic PHV demand dataset
if __name__ == "__main__":
    try:
        print("Starting the synthetic PHV demand generation process.")
        df = generate_synthetic_phv_demand()
        print("Process completed successfully.")
    except Exception as e:
        print("Critical Error during execution:", e)

