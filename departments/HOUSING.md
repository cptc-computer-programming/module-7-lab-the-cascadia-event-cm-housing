## 🏠 Department of Housing

### Situation

Thousands of residents have been displaced from their homes. Lakewood has opened emergency shelters across the region, but space is limited and new arrivals continue each hour.

### Mission

Write a Python program to collect and analyze shelter occupancy data for each district and each shelter.

### Data Collected

For each shelter, collect:

- Total shelter capacity
- Number of people currently sheltered
- Number of new evacuees expected

### Requirements

Your program must:

- Use an outer loop to process two districts.
- Use an inner loop to process three shelters per district.
- Validate all input values.

### Input Limits

| Input | Valid Values |
|---|---|
| Total capacity | Greater than 0 |
| People sheltered | Greater than 0 and less than or equal to total capacity |
| New evacuees expected | 0 or greater |

### Calculations

Occupancy rate for each shelter:

    occupancy_rate = people_sheltered / total_capacity * 100

Average occupancy rate:

    average_occupancy = total_occupancy_rates / 3

Projected occupancy rate:

    projected_occupancy = (total_sheltered + total_new_evacuees) / total_capacity * 100

### Outputs

Your program must display:

- Occupancy rate for each shelter
- Average occupancy rate for each district
- Total capacity for each district
- Total people sheltered for each district
- Total new evacuees expected for each district
- Projected occupancy rate for each district

### Metric Reported to City Manager

At the end of the program, your team must report:

| District | Metric |
|---|---|
| Clover Park | Average occupancy rate |
| Steilacoom | Average occupancy rate |

### Sample Output
```
*** District 1 (Clover Park) ***

-- Shelter 1 Data --
Enter total capacity: 150
Enter people sheltered: 120
Enter new evacuees expected: 20
Occupancy rate: 80.0%

-- Shelter 2 Data --
Enter total capacity: 200
Enter people sheltered: 180
Enter new evacuees expected: 25
Occupancy rate: 90.0%

-- Shelter 3 Data --
Enter total capacity: 100
Enter people sheltered: 85
Enter new evacuees expected: 10
Occupancy rate: 85.0%

*** District Summary ***
-------------------
Average occupancy rate: 85.00%
Total capacity: 450
Total sheltered: 385
Total new evacuees expected: 55
Projected occupancy rate: 97.56%


*** District 2 (Steilacoom) ***

-- Shelter 1 Data --
Enter total capacity: 180
Enter people sheltered: 150
Enter new evacuees expected: 25
Occupancy rate: 83.3%

-- Shelter 2 Data --
Enter total capacity: 220
Enter people sheltered: 200
Enter new evacuees expected: 40
Occupancy rate: 90.9%

-- Shelter 3 Data --
Enter total capacity: 150
Enter people sheltered: 130
Enter new evacuees expected: 15
Occupancy rate: 86.7%

*** District Summary ***
-------------------
Average occupancy rate: 86.97%
Total capacity: 550
Total sheltered: 480
Total new evacuees expected: 80
Projected occupancy rate: 101.82% 


Data collection complete for all districts.
```