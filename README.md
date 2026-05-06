# Lakewood Emergency Operations Center

## Overview

Two days after a major Cascadia Subduction Zone earthquake, the City of Lakewood is operating under emergency conditions. Roads are damaged, power is unreliable, water systems are compromised, and emergency shelters are nearing capacity.

Your team has been assigned to one department in the Lakewood Emergency Operations Center. Your job is to write a Python program that collects department-specific emergency data, validates the input, performs calculations, and prints a district-level summary.

At the end of the lab, each department will report its final metrics to the City Manager. The class will then combine the results into a citywide emergency coordination report.

---

## Learning Outcomes

By the end of this lab, you should be able to:

1. Use `for` loops to repeat a known number of times.
2. Use nested loops to process multiple districts and multiple data entries within each district.
3. Use `while` loops to validate user input.
4. Use running totals and counters to calculate totals, averages, and percentages.
5. Apply formulas inside and after loops.
6. Format program output clearly for a user.
7. Explain how department-level data contributes to a citywide emergency response decision.

---

## Team Assignment

Your instructor will assign your team to one department.

Each team completes only the Python file for its assigned department.

| Department | File |
|---|---|
| Department of Energy | `energy.py` |
| Department of Transportation | `transportation.py` |
| Department of Water | `water.py` |
| Department of Housing | `housing.py` |

Do not complete the other department files unless otherwise instructed.

---

## Districts

Every department will process the same two districts:

1. Clover Park
2. Steilacoom

Your program must use an outer loop to process both districts.

## General Program Structure

Each department program must follow this general structure:

1. Print a title for the department.
2. Use an outer loop to process two districts.
3. Use an inner loop to process three routes, shelters, or time periods.
4. Collect the required input values.
5. Validate every input using a `while` loop.
6. Calculate and display an item-level result.
7. Use running totals to track district-level data.
8. After the inner loop ends, calculate district-level results.
9. Print a clear district summary.
10. After both districts are complete, print a final completion message.

## Input Validation Requirement

Every numeric input must be validated with a `while` loop.

If the user enters an invalid value, your program must:

1. Display an error message.
2. Ask for the value again.
3. Continue repeating until the value is valid.

A single `if` statement is not enough for this lab.

Example validation loop:

    duration = float(input("Enter outage duration (0-24 hours): "))

    while duration < 0 or duration > 24:
        print("Error: duration must be between 0 and 24.")
        duration = float(input("Enter outage duration (0-24 hours): "))

---

# Citywide Integration

After all department programs are complete, each team will report its final district metrics to the City Manager.

The City Manager will enter these values into the City Integration Program.

The citywide report will use the department metrics to evaluate the overall condition of each district.

| Department | Metric | Desired Direction |
|---|---|---|
| Transportation | Average evacuation time | Lower is better |
| Energy | Average outage duration | Lower is better |
| Water | District gallons per person | Higher is better |
| Housing | Average shelter occupancy rate | Moderate is best |
