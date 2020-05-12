import setuptools
import sys

needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="grocer-notifier",
    description="Automatic alerts when your grocery delivery service has delivery times available",
    long_description=long_description,
    author="John Ward",
    author_email="john@johnward.io",
    url="https://github.com/itsjohnward/grocer-notifier",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "twilio",
        "grocer @ git+https://git@github.com/itsjohnward/grocer@v0.2.0#egg=grocer",
    ],
    # root must be current directory
    # otherwise, use_scm_version = {"root": path, "relative_to": __file__}
    use_scm_version=True,
    setup_requires=pytest_runner + ["setuptools_scm"],
    test_suite="pytest",
    tests_require=[],
    entry_points={"console_scripts": ["grocerytime=notifier.__main__:main"]},
)
