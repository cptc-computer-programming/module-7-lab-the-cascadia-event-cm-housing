# Lakewood Emergency Operations Center
# Department of Housing


# Declared Constant Variables.
DISTRICT_COUNT = 2
SHELTER_COUNT = 3

MIN_CAPACITY = 1
MIN_PEOPLE_SHELTERED = 1
MIN_NEW_EVACUEES = 0

PERCENTAGE_RATE = 100



# The start of our loop over our districts.
for district in range (1, 3):

    # Shelter data intiated variables.
    total_capacity = 0
    people_sheltered = 0
    new_evacuees_expected = 0
    occupancy_rate = 0
    average_occupancy_rate_for_district = 0
    calc_occupancy_rate = 0
# yo
    # The start of our loop for our shelters.
    for shelters in range(3):

        # Total Capacity.
        user_total_capacity = int(input("Enter Total Capacity: "))
        while user_total_capacity < MIN_CAPACITY:
            user_total_capacity = int(input("Invalid Entry. Please Enter Valid Total Capacity: "))
        total_capacity += user_total_capacity
        
        #People Sheltered.
        user_people_sheltered = int(input("Enter people sheltered: "))
        while user_people_sheltered < MIN_PEOPLE_SHELTERED and user_people_sheltered <= user_total_capacity:
            user_people_sheltered =int(input("Invalid Entry. Please Enter Valid People Sheltered: "))
        people_sheltered += user_people_sheltered

        # New Expected Evacuees.
        user_new_evacuees_expected = int(input("Enter New Evacuees Expected: "))
        while user_new_evacuees_expected >= MIN_NEW_EVACUEES:
            user_new_evacuees_expected = int(input("Invalid Entry. Please Enter Valid New Evacuees Expected: "))
        new_evacuees_expected += user_new_evacuees_expected

        # Occupancy rates for each shelter and district.
        calc_occupancy_rate = people_sheltered / total_capacity * PERCENTAGE_RATE
        occupancy_rate += calc_occupancy_rate
    
    # Summary for the district.
    print(f"*** District {district} Summary ***")
    print("-------------------")
    print("Average occupancy rate: %", (occupancy_rate / 3))
    print("Total Capacity: ", total_capacity)
    print("Total sheltered: ", people_sheltered)
    print("Total new evacuees expected: ", new_evacuees_expected)
    print("Projected occupancy rate: %",(people_sheltered + new_evacuees_expected) / total_capacity * PERCENTAGE_RATE)

# Ending message for program.
print("Data collection complete for all districts.")
print("```")
