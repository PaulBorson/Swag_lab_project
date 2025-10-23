import os
import glob
import pytest
from datetime import datetime
import multiprocessing
from pathlib import Path


def run_tests():
    # Test discovery
    test_files = glob.glob("test/test_*.py")
    num_test_files = len(test_files)
    cpu_cores = multiprocessing.cpu_count()
    if num_test_files > cpu_cores:
        num_test_files = cpu_cores

    # Report folder
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"reports/report_{timestamp}.html"

    # Pytest arguments
    pytest_args = [
        *test_files,
        "-n", str(num_test_files),
        "--html", report_name,
        "--self-contained-html",
        "-v"
    ]

    print(f"🧪 Running {len(test_files)} test files using {num_test_files} cores...")
    pytest.main(pytest_args)

    # ✅ Inject summary table
    add_summary_to_html(report_name)


def add_summary_to_html(report_path):
    """Adds a summary section to the pytest HTML report after tests finish."""
    report_file = Path(report_path)
    if not report_file.exists():
        print("⚠️ Report not found. Skipping summary injection.")
        return

    with open(report_file, "r", encoding="utf-8") as f:
        html = f.read()

    # ✅ Create custom summary section
    summary_html = """
    <h2 style="margin-top:30px; color:#333;">🧩 Test Dependency Summary</h2>
    <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; width:100%; font-family:Arial;">
        <tr style="background-color:#f2f2f2;">
            <th>Test Name</th>
            <th>Depends On</th>
            <th>Status</th>
            <th>Notes</th>
        </tr>
        <tr><td>test_add_product</td><td>None</td><td>✅ Pass / ❌ Fail</td><td>Main flow start</td></tr>
        <tr><td>test_checkout_cencel</td><td>test_add_product</td><td>✅ Pass / ⚠️ Skip</td><td>Cancel checkout flow</td></tr>
        <tr><td>test_checkout_confirm</td><td>test_checkout_cencel</td><td>✅ Pass / ⚠️ Skip</td><td>Final confirmation</td></tr>
    </table>

    <p style="margin-top:10px; font-style:italic; color:#555;">
        💡 <b>Note:</b> If a dependency test fails, all dependent tests will be automatically skipped.
    </p>
    """

    # ✅ Inject before </body>
    if "</body>" in html:
        html = html.replace("</body>", summary_html + "</body>")

    # Write back
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Summary table added to {report_path}")


if __name__ == "__main__":
    run_tests()
