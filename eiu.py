def unpack_log(file):
    """Unpacks a log file into a list of dictionaries.

    Args:
        file: The log file to unpack.

    Returns:
        A list of dictionaries, each representing a log entry.
    """

    log_entries = []
    with open(file, "r") as f:
        for line in f:
            try:
                log_entry = json.loads(line)
                log_entries.append(log_entry)
            except json.JSONDecodeError:
                continue

    return log_entries

