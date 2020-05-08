import os
import subprocess

import conducto as co

def run_tests():
    """
    This code is run by the worker nodes. It goes through the list of tests to run,
    checks the temp_data store to see if another node is running it, then if not, writes
    its own placeholder to the temp_data store and runs the test.

    A one-line summary is printed for each successful test, but the entire test output is
    printed if there is a failure.

    The worker's name and the test output are written to the temp_data store when the test
    run is complete for use in the summary.

    Note that there is a small chance for a race condition here: at the point one worker has
    selected a particular test to run, but before it has written to the temp_data store, another
    worker could choose to run the same test. To fix this properly would require some queueing
    mechanism, which would be a nice service for Conducto to provide.
    """
    host = os.environ.get("WORKER_NAME").encode("utf-8")

    test_files = sorted([ f for f in os.listdir("./test") 
                          if f.startswith("test") and f.endswith(".py") ])
    for test_file in test_files:
        if co.temp_data.exists(f"test_run/{test_file}"): continue
        co.temp_data.puts(f"test_run/{test_file}", host)
        result = run_test(test_file)
        co.temp_data.puts(f"test_run/{test_file}", host + b"\n" + result)

def run_test(test_file):
    print(f"Running test {test_file}: ", end='')
    cmd = ["python", "-m", "unittest", test_file]
    completed = subprocess.run(cmd, cwd="./test", capture_output=True)
    result = completed.stderr.decode("utf-8")
    status = result.splitlines()[-1]
    if status.startswith("FAILED"):
        print(f"\n{result}")
    else:
        print(status)
    return completed.stderr

if __name__ == "__main__":
    run_tests()