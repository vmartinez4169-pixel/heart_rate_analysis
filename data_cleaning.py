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