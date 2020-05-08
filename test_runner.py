import conducto as co
import time

MAX_WORKERS = 3

def run_tests() -> co.Serial:
    """
    Parallel Test Runner Demo

    This is the code to run the parallel test runner demo. It is invoked with the command

    python test_runner.py run_tests --local --run

    Please see the README.md file for a full explanation.
    """
    image = co.Image("python:3.8", copy_dir="./code", reqs_py=["conducto"])

    with co.Serial(image=image) as pipeline:

        with co.Parallel(name="run_tests") as run_tests: 
            for worker_num in range(MAX_WORKERS):
                run_tests[f"worker{worker_num:02}"] = co.Exec("python run_tests.py",
                                                               env={ "WORKER_NAME": f"worker{worker_num:02}"})
                time.sleep(0.1)

        pipeline["summary"] = co.Exec("python print_summary.py")

    return pipeline

if __name__ == "__main__":
    co.main()


