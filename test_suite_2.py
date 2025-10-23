import os
import glob
import pytest
from datetime import datetime



test_files = glob.glob("test/test_*.py")
num_test_files = len(test_files)
import multiprocessing
cpu_cores = multiprocessing.cpu_count()
if num_test_files > cpu_cores:
    num_test_files = cpu_cores

def run_tests():
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"reports/report_{timestamp}.html"
    pytest_args = [
        *test_files,
        "-n",str(num_test_files),
        #"-m", "smoke",
        #"--html=reports/report.html",
        "--html", report_name,
        "--self-contained-html",
        "-v"
    ]
    pytest.main(pytest_args)

if __name__ == "__main__":
    run_tests()