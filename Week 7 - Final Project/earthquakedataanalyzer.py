import pandas as pd

# Earthquake Data Analyzer
# This script loads earthquake data from a CSV file and provides basic functionality to analyze it.

# Constants
FILE_PATH = f"earthquake_data_largest.csv"

def main():
    # Load earthquake data
    earthquake_data = load_data(FILE_PATH)
    analyze_data(earthquake_data)

def load_data(file_path):
    """
    Load earthquake data from a CSV file.
    
    :param file_path: Path to the CSV file containing earthquake data.
    :return: DataFrame containing the earthquake data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def analyze_data(data):
    """
    Analyze the earthquake data.
    
    :param data: DataFrame containing the earthquake data.
    :return: None
    """
    if data is not None:
        print("Data loaded successfully.")
        print("First few records:")
        print(data.head())

        # Statistical summary of the data
        print("\nStatistical summary of the data:")
        frequency_analysis(data)
        magnitude_analysis(data)
        depth_analysis(data)
        geographical_analysis(data)

        # Temporal and historical analysis
        temporal_patterns(data)
        historical_insights(data)

        print("\nData analysis complete.")
    else:
        print("No data to analyze.")

def frequency_analysis(data):
    """
    Perform frequency analysis on the earthquake data.
    
    :param data: DataFrame containing the earthquake data.
    :return: None
    """
    if data is not None:
        print("\nFrequency Analysis:")
        # Calculate the total number of earthquakes in the dataset.
        total_earthquakes = len(data)
        print(f"Total number of earthquakes: {total_earthquakes}")

        # Determine how many earthquakes occur per year, month, or even day if the data is dense enough.
        if 'Year' in data.columns:
            earthquakes_per_year = data['Year'].value_counts().sort_index()
            print("Number of earthquakes per year:")
            print(earthquakes_per_year)
        
        # Analyze trends over decades or centuries if applicable.
        if 'Year' in data.columns:
            decade_counts = (data['Year'] // 10 * 10).value_counts().sort_index()
            print("Number of earthquakes per decade:")
            print(decade_counts)
    else:
        print("No data to analyze.")

def magnitude_analysis(data):
    """
    Perform magnitude analysis on the earthquake data.
    
    :param data: DataFrame containing the earthquake data.
    :return: None
    """
    if data is not None:
        print("\nMagnitude Analysis:")
        if 'Mag' in data.columns:
            # Find the average, minimum, and maximum magnitudes of the earthquakes.
            average_magnitude = data['Mag'].mean()
            min_magnitude = data['Mag'].min()
            max_magnitude = data['Mag'].max()
            print(f"Average Magnitude: {round(average_magnitude, 2)}")
            print(f"Minimum Magnitude: {min_magnitude}")
            print(f"Maximum Magnitude: {max_magnitude}")

            # Count the number of earthquakes above various magnitude thresholds (e.g., 7.0, 7.5, 8.0).
            thresholds = [5.0, 6.0, 7.0, 8.0]
            for threshold in thresholds:
                count_above_threshold = (data['Mag'] >= threshold).sum()
                print(f"Number of earthquakes with magnitude >= {threshold}: {count_above_threshold}")
        else:
            print("Magnitude column not found in the data.")
    else:
        print("No data to analyze.")

def depth_analysis(data):
    """
    Perform depth analysis on the earthquake data.
    
    :param data: DataFrame containing the earthquake data.
    :return: None
    """
    if data is not None:
        print("\nDepth Analysis:")
        if 'Depth' in data.columns:
            # Calculate the average depth of earthquakes.
            average_depth = data['Depth'].mean()
            print(f"Average Depth: {round(average_depth, 2)} km")

            # Identify the shallowest and deepest earthquakes.
            min_depth = data['Depth'].min()
            max_depth = data['Depth'].max()
            print(f"Shallowest Earthquake Depth: {min_depth} km")
            print(f"Deepest Earthquake Depth: {max_depth} km")

            # Analyze the distribution of earthquake depths (e.g., count how many occur at shallow vs. deep levels).
            shallow_count = (data['Depth'] < average_depth).sum()  # Shallow earthquakes
            deep_count = (data['Depth'] >= average_depth).sum()
            print(f"Number of shallow earthquakes (depth < average): {shallow_count}")
            print(f"Number of deep earthquakes (depth >= average): {deep_count}")
        else:
            print("Depth column not found in the data.")
    else:
        print("No data to analyze.")

def geographical_analysis(data):
    """
    Perform geographical analysis on the earthquake data.
    
    :param data: DataFrame containing the earthquake data.
    :return: None
    """
    if data is not None:
        print("\nGeographical Analysis:")
        if ('Lat' in data.columns) and ('Lon' in data.columns):
            # Determine which region experienced the most earthquakes.
            region_counts = data.groupby(['Lat', 'Lon']).size().reset_index(name='Counts')
            most_frequent_region = region_counts.loc[region_counts['Counts'].idxmax()]
            print(f"Region with most earthquakes: Latitude {most_frequent_region['Lat']}, Longitude {most_frequent_region['Lon']} with {most_frequent_region['Counts']} occurrences.")
            
            # Count earthquakes per region and identify the most seismically active areas.
            active_regions = data.groupby(['Lat', 'Lon']).size().reset_index(name='Counts')
            active_regions = active_regions.sort_values(by='Counts', ascending=False)
            print("Most seismically active regions:")
            print(active_regions.head(10))
        else:
            print("Latitude and Longitude columns not found in the data.")
    else:
        print("No data to analyze.") 

def temporal_patterns(data):
    """
    Analyze temporal patterns in the earthquake data.
    
    :param data: DataFrame containing the earthquake data.
    :return: None
    """
    if data is not None:
        print("\nTemporal Patterns:")
        # Identify any seasonal patterns in earthquake occurrences.
        monthly_counts = data['Month'].value_counts().sort_index()
        print("Number of earthquakes per month:")
        print(monthly_counts)

        # Look for patterns over the years to see if earthquake magnitude is increasing or decreasing.
        average_magnitude_per_year = data.groupby('Year')['Mag'].mean()
        print("Average magnitude per year:")
        print(average_magnitude_per_year)
    else:
        print("No data to analyze.")

def historical_insights(data):
    """
    Provide historical insights based on the earthquake data.
    
    :param data: DataFrame containing the earthquake data.
    :return: None
    """
    if data is not None:
        print("\nHistorical Insights:")
        # Determine the year with the highest total earthquake magnitude (sum of all magnitudes within a year).
        if 'Year' in data.columns and 'Mag' in data.columns:
            yearly_magnitude_sum = data.groupby('Year')['Mag'].sum().sort_values(ascending=False)
            highest_year = yearly_magnitude_sum.idxmax()
            highest_magnitude = yearly_magnitude_sum.max()
            print(f"Year with highest total earthquake magnitude: {highest_year} with a total magnitude of {highest_magnitude}")

        # Display significant historical earthquake events.
        if 'Year' in data.columns and 'Mag' in data.columns:
            significant_events = data[data['Mag'] >= 7.0]
            print("Significant historical earthquake events:")
            print(significant_events[['Year', 'Month', 'Depth', 'Mag', 'Region']].sort_values(by = 'Mag', ascending=False).head(10))
    else:
        print("No data to analyze.")

if __name__ == "__main__":
    main()