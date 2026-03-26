import matplotlib.pyplot as plt


def plot_line_chart(data: list, output_file: str):
    """
    Create and save a line plot from the heart rate data.
    """
    plt.figure()
    plt.plot(data)
    plt.title('Heart Rate Over Time')
    plt.xlabel("Reading Order")
    plt.ylabel("Heart Rate (BPM)")
    plt.savefig(output_file)
    plt.close()