## 🚦 Department of Transportation

### Situation

Lakewood’s primary evacuation routes have suffered damage from landslides, debris, and congestion. Travel times have increased dramatically, slowing evacuation efforts.

### Mission

Write a Python program to collect and analyze evacuation data for each district and each evacuation route.

### Data Collected

For each route, collect:

- Evacuation travel time in minutes
- Route distance in miles
- Number of vehicles evacuated

### Requirements

Your program must:

- Use an outer loop to process two districts.
- Use an inner loop to process three routes per district.
- Validate all input values.

### Input Limits

| Input | Valid Values |
|---|---|
| Travel time | 5 to 300 minutes |
| Route distance | Greater than 0 miles |
| Vehicles evacuated | Greater than 0 |

### Calculations

Average speed for each route:
```
    speed = distance / (travel_time / 60)
```
District average evacuation time:
```
    average_time = total_travel_time / 3
```
District average route distance:
```
    average_distance = total_distance / 3
```
Evacuation efficiency:
```
    efficiency = total_vehicles / total_travel_time
```
### Outputs

Your program must display:

- Average speed for each route
- Average evacuation time for each district
- Average route distance for each district
- Total vehicles evacuated for each district
- Evacuation efficiency for each district

### Metric Reported to City Manager

At the end of the program, your team must report:

| District | Metric |
|---|---|
| Clover Park | Average evacuation time |
| Steilacoom | Average evacuation time |

### Sample Output
```
*** District 1 (Clover Park)***

-- Route 1 Data --
Enter travel time (5–300 minutes): 120
Enter route distance (miles): 50
Enter number of vehicles evacuated: 400


Average speed for Route 1: 25.0 mph

-- Route 2 Data --
Enter travel time (5–300 minutes): 180
Enter route distance (miles): 60
Enter number of vehicles evacuated: 350


Average speed for Route 2: 20.0 mph

-- Route 3 Data --
Enter travel time (5–300 minutes): 150
Enter route distance (miles): 55
Enter number of vehicles evacuated: 500
   ➜ Average speed for Route 3: 22.0 mph

*** District Summary ***
-------------------
Average evacuation time: 150.00 minutes
Average route distance: 55.00 miles
Total vehicles evacuated: 1250
Evacuation efficiency: 8.33 vehicles per minute


*** District 2 (Steilacoom) ***

-- Route 1 Data --
Enter travel time (5–300 minutes): 200
Enter route distance (miles): 80
Enter number of vehicles evacuated: 600


Average speed for Route 1: 24.0 mph

-- Route 2 Data --
Enter travel time (5–300 minutes): 250
Enter route distance (miles): 90
Enter number of vehicles evacuated: 700


Average speed for Route 2: 21.6 mph

-- Route 3 Data --
Enter travel time (5–300 minutes): 300
Enter route distance (miles): 100
Enter number of vehicles evacuated: 650


Average speed for Route 3: 20.0 mph

*** District Summary ***
-------------------
Average evacuation time: 250.00 minutes
Average route distance: 90.00 miles
Total vehicles evacuated: 1950
Evacuation efficiency: 7.80 vehicles per minute


Data collection complete for all districts.
```