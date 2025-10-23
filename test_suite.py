import os
import pytest

def run_tests():
    os.makedirs("reports", exist_ok=True)
    pytest_args = [
        "test/test_add_product.py",
        "test/test_checkout_cencel.py",
        "-m", "smoke",
        "--html=reports/report.html",
        "--self-contained-html",
        "-v"
    ]
    pytest.main(pytest_args)

if __name__ == "__main__":
    run_tests()
