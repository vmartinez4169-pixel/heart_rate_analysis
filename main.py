def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_list = []
    removed_values = 0

    for row in data:
        row = row.strip()

        if row.isdigit():
            value = int(row)

            if value >= 30 and value <= 220:
                cleaned_list.append(value)
            else:
                removed_values += 1
        else:
            removed_values += 1

    return cleaned_list, removed_values


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0

    for value in data:
        total = total + value

    return total / len(data)


def median(data: list) -> float:
    """
    Calculate the median value of a clean list of heart-rate readings.
    """
    data = sorted(data)

    n = len(data)
    middle = n // 2

    if n % 2 == 1:
        return data[middle]
    else:
        return (data[middle - 1] + data[middle]) / 2


def range(data: list) -> float:
    """
    Calculate the range of a clean list of heart-rate readings.
    """
    highest = max(data)
    lowest = min(data)

    return highest - lowest


def rolling_avg(data: list, k: int) -> list:
    """
    CHALLENGE FUNCTION (Optional)
    """
    averages = []

    for i in range(len(data) - k + 1):
        total = 0

        for j in range(i, i + k):
            total = total + data[j]

        avg = total / k
        averages.append(avg)

    return averages


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
    cleaned_list, removed_values = clean_heartrate_data(data)

    # calculate the average, median, and range of this file using the functions you've wrote
    avg_val = round(average(cleaned_list), 2)
    med_val = round(median(cleaned_list), 2)
    range_val = round(range(cleaned_list), 2)

    # print out your data quality measure to the console
    print("File:", file)
    print("Removed values:", removed_values)

    # print out your descriptive statistics to the console
    print("Average heart rate:", avg_val)
    print("Median heart rate:", med_val)
    print("Range of heart rates:", range_val)

    return avg_val, med_val, range_val


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")