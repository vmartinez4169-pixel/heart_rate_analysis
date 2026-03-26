import data_analysis
import data_cleaning
import data_visualizations


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    with open(file, "r") as file_obj:
        data = file_obj.readlines()

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = data_cleaning.clean_heartrate_data(data)

    # calculate the average, median, range, variance, and standard deviation of this file using these functions.
    avg_val = round(data_analysis.average(cleaned_list), 2)
    med_val = round(data_analysis.median(cleaned_list), 2)
    range_val = round(data_analysis.range(cleaned_list), 2)
    var_val = round(data_analysis.variance(cleaned_list), 2)
    std_val = round(data_analysis.standard_deviation(cleaned_list), 2)

    # create and save line plot image
    filename = file.replace("data/", "images/").replace(".txt", ".png")
    data_visualizations.plot_line_chart(cleaned_list, filename)
    print("Saved image to:", filename)

    # print out your data quality measure to the console
    print("File:", file)
    print("Removed values:", removed_values)

    # print out your descriptive statistics to the console
    print("Average heart rate:", avg_val)
    print("Median heart rate:", med_val)
    print("Range of heart rates:", range_val)
    print("Variance:", var_val)
    print("Standard deviation:", std_val)


    return avg_val, med_val, range_val, var_val, std_val


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")