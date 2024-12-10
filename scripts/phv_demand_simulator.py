# Script to generate synthetic hourly PHV demand for a one-week period with error handling.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_synthetic_phv_demand(start_date='2024-12-09', end_date='2024-12-15'):
    """
    Generates a synthetic dataset representing the hourly demand for Private Hire Vehicles (PHV) over a one-week period.
    
    Parameters:
    - start_date (str): The start date for the dataset in the format 'YYYY-MM-DD'.
    - end_date (str): The end date for the dataset in the format 'YYYY-MM-DD'.
    
    Returns:
    - DataFrame: A Pandas DataFrame containing the synthetic PHV demand data.
    """
    try:
        # Get the path to the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Set the path to the /data/ directory
        data_dir = os.path.join(script_dir, '../data')

        # Step 1: Create the /data/ directory if it does not exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            print(f"Directory '{data_dir}' created successfully.")
        
        # Set random seed for reproducibility
        np.random.seed(42)
        
        # Step 2: Generate hourly timestamps
        fechas = pd.date_range(start=start_date, end=end_date, freq='H')
        if fechas.empty:
            raise ValueError("The date range is empty. Please check your start_date and end_date.")

        # Step 3: Generate synthetic demand data
        demand = []
        for fecha in fechas:
            hour = fecha.hour
            day_of_week = fecha.dayofweek

            if day_of_week < 5:
                if 7 <= hour < 9 or 17 <= hour < 19:
                    base_demand = 80
                else:
                    base_demand = 30
            else:
                if 20 <= hour or hour < 2:
                    base_demand = 70
                else:
                    base_demand = 40

            demand_hour = np.random.poisson(lam=base_demand)
            demand.append(demand_hour)

        # Step 4: Create DataFrame with demand data
        df = pd.DataFrame({'datetime': fechas, 'demand': demand})
        df['hour'] = df['datetime'].dt.hour
        df['day_of_week'] = df['datetime'].dt.dayofweek

        if df.empty:
            raise ValueError("The DataFrame is empty. Please review the data generation logic.")

        # Step 5: Save the DataFrame to a CSV file in the /data/ directory
        csv_path = os.path.join(data_dir, 'synthetic_phv_demand.csv')
        df.to_csv(csv_path, index=False)
        if not os.path.isfile(csv_path):
            raise IOError(f"File '{csv_path}' could not be created.")
        
        print(f"Data successfully saved to {csv_path}")

        # Step 6: Generate heatmap
        print("Creating heatmap to visualize hourly demand distribution by day of the week.")
        
        demand_by_day_hour = df.groupby(['day_of_week', 'hour'])['demand'].sum().reset_index()
        total_demand_by_day = df.groupby('day_of_week')['demand'].sum().reset_index()
        demand_by_day_hour = demand_by_day_hour.merge(total_demand_by_day, on='day_of_week', suffixes=('', '_total'))
        demand_by_day_hour['percentage'] = (demand_by_day_hour['demand'] / demand_by_day_hour['demand_total']) * 100

        # Pivot the data to create a matrix for the heatmap
        heatmap_data = demand_by_day_hour.pivot(index='day_of_week', columns='hour', values='percentage')

        # Step 7: Plot and save the heatmap as an image file in the /data/ directory
        plt.figure(figsize=(12, 6))
        sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt=".1f", cbar=True)
        plt.title('PHV Demand Distribution by Hour and Day of the Week (%)')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Day of the Week (0 = Monday, 6 = Sunday)')

        png_path = os.path.join(data_dir, 'phv_demand_heatmap.png')
        plt.savefig(png_path)
        plt.close()

        print(f"Heatmap image successfully saved to {png_path}")

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


