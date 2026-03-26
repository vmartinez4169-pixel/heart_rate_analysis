import statistics as stats


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    average = stats.mean(data)
    return average


def median(data: list) -> float:
    """
    Calculate the median value of a clean list of heart-rate readings.
    """
    median = stats.median(data)
    return median


def range(data: list) -> float:
    """
    Calculate the range of a clean list of heart-rate readings.
    """
    highest = max(data)
    lowest = min(data)

    return highest - lowest


def variance(data: list) -> float:
    """
    Calculate the variance of a clean list of heart-rate readings.
    """
    variance = stats.variance(data)
    return variance


def standard_deviation(data: list) -> float:
    """
    Calculate standard deviation using variance.
    """
    standard_deviation = stats.stdev(data)
    return standard_deviation


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