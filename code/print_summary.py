import conducto as co

def print_summary():
    """
    This code is run by the summary node. It reads all the test runs from
    the temp_data store and prints out a summary.
    """
    keys = sorted(co.temp_data.list("test_run"))
    for key in keys:
        test = key[9:] # chop "test_run/" prefix
        result = co.temp_data.gets(key).decode("utf-8").splitlines()
        host = result[0]
        status = result[-1]
        print(f"{test}:\t{host}\t{status}")


if __name__ == "__main__":
    print_summary()