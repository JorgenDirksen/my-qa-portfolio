# first_script.py
# My first Python script for QA purposes

print("QA Engineer - Practical Testing to Automation")
print("=" * 50)

# Example: A simple list of test scenarios I might automate
test_scenarios = [
    "User Login Validation",
    "Search Functionality Check",
    "API Endpoint Health Check",
    "Form Submission with Invalid Data"
]

print("Test scenarios to automate:")
for number, scenario in enumerate(test_scenarios, start=1):
    print(f"{number}. {scenario}")

print("=" * 50)
print("Next step: Learn Selenium WebDriver to automate these.")
