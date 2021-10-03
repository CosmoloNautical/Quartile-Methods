def get_quartiles(dataset, method):

    """
    Given a list of numbers and a method (T, MM or MS) this program will return the quartiles using the given method
    """


    import statistics
    dataset.sort()
    quartiles_arr = [dataset[0], 0, statistics.median(dataset), 0, dataset[len(dataset) - 1]]
    if method == "T" or method == "MM":
        dataset_lower = []
        dataset_higher = []
        if len(dataset) % 2 != 0 and method == "T":
            dataset.insert(dataset.index(quartiles_arr[2]), quartiles_arr[2])
        elif len(dataset) % 2 != 0 and method == "MM":
            dataset.pop(dataset.index(quartiles_arr[2]))
        for data in range(0, int(len(dataset) / 2)):
            dataset_lower.append(dataset[data])
        for data in range(int(len(dataset) / 2), len(dataset)):
            dataset_higher.append((dataset[data]))
        quartiles_arr[1], quartiles_arr[3] = statistics.median(dataset_lower), statistics.median(dataset_higher)
    elif method == "MS":
        quartiles_arr[1], quartiles_arr[3] = dataset[round((len(dataset) + 1) / 4) - 1], dataset[
            round(3 * (len(dataset) + 1) / 4) - 1]
    return quartiles_arr
