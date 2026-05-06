print("City of Lakewood Emergency Coordination Center")
print("==============================================")
print("This program combines district reports from all departments.\n")

districts = ["Clover Park", "Steilacoom"]

evac_times = []
power_outages = []
water_supply = []
occupancy_rates = []

# Collect data for each district
for district in districts:
    print(f"\nEnter data for {district} District")

    evac = float(input("Average evacuation time (minutes): "))
    power = float(input("Average outage duration (hours): "))
    water = float(input("Average gallons per person: "))
    occ = float(input("Average shelter occupancy rate (%): "))

    evac_times.append(evac)
    power_outages.append(power)
    water_supply.append(water)
    occupancy_rates.append(occ)

# Process and report results
print("\nCity of Lakewood District Recovery Summary")
print("==============================================")

for i in range(len(districts)):
    district = districts[i]
    evac = evac_times[i]
    power = power_outages[i]
    water = water_supply[i]
    occ = occupancy_rates[i]

    # Health Index Formula
    # Lower evac/power = better; higher water/occupancy = better
    health_index = (100 / evac) + (100 / (power + 1)) + (water * 2) + (occ / 2)

    print(f"\n{district} District Report")
    print("-------------------------------------------")
    print(f"Evacuation time: {evac:.1f} minutes")
    print(f"Power outage: {power:.1f} hours")
    print(f"Water supply: {water:.1f} gallons/person")
    print(f"Shelter occupancy: {occ:.1f}%")
    print(f"District Health Index: {health_index:.2f}")

    # Status interpretation
    if health_index >= 250:
        print("Status: Stable")
    elif 150 <= health_index < 250:
        print("Status: Moderate stress – assistance required")
    else:
        print("Status: Critical – deploy additional resources")

print("\nEnd of Emergency Coordination Report")
