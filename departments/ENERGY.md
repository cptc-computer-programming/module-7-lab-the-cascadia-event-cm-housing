## ⚡ Department of Energy

### Situation

Widespread power outages have affected nearly all of Lakewood. Substations sustained damage, and transmission lines have been disrupted by fallen debris.

### Mission

Write a Python program to collect and analyze power outage data for each district and each time period.

### Data Collected

For each time period, collect:

- Duration of outage in hours
- Number of affected households
- Number of households restored during the period

### Requirements

Your program must:

- Use an outer loop to process two districts.
- Use an inner loop to process three time periods per district:
  - Morning
  - Afternoon
  - Night
- Validate all input values.

### Input Limits

| Input | Valid Values |
|---|---|
| Outage duration | 0 to 24 hours |
| Affected households | Greater than 0 |
| Restored households | 0 or greater and less than or equal to affected households |

### Calculations

Percent restored for each time period:
```
    percent_restored = restored_households / affected_households * 100
```
Average outage duration:
```
    average_outage = total_outage_duration / 3
```
Overall restoration rate:
```
    overall_restoration = total_restored / total_affected * 100
```
### Outputs

Your program must display:

- Percent restored for each time period
- Average outage duration for each district
- Total households affected for each district
- Total households restored for each district
- Overall restoration rate for each district

### Metric Reported to City Manager

At the end of the program, your team must report:

| District | Metric |
|---|---|
| Clover Park | Average outage duration |
| Steilacoom | Average outage duration |

### Sample Output
```
*** District 1 (Clover Park) ***

-- Morning Period --
Enter outage duration (0–24 hours): 8
Enter affected households: 500
Enter restored households: 200
Percent restored: 40.0%

-- Afternoon Period --
Enter outage duration (0–24 hours): 6
Enter affected households: 400
Enter restored households: 300
Percent restored: 75.0%

-- Night Period --
Enter outage duration (0–24 hours): 10
Enter affected households: 600
Enter restored households: 450
Percent restored: 75.0%

*** District Summary ***
-------------------
Average outage duration: 8.00 hours
Total households affected: 1500
Total households restored: 950
Overall restoration rate: 63.33%


*** District 2 (Steilacoom) ***

-- Morning Period --
Enter outage duration (0–24 hours): 12
Enter affected households: 800
Enter restored households: 300
Percent restored: 37.5%

-- Afternoon Period --
Enter outage duration (0–24 hours): 9
Enter affected households: 500
Enter restored households: 200
Percent restored: 40.0%

-- Night Period --
Enter outage duration (0–24 hours): 11
Enter affected households: 700
Enter restored households: 400
Percent restored: 57.1%

*** District Summary ***
-------------------
Average outage duration: 10.67 hours
Total households affected: 2000
Total households restored: 900
Overall restoration rate: 45.00%


Data collection complete for all districts.
```