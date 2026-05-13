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
for districts in range (2):

    # Shelter data intiated variables.
    total_capacity = 0
    people_sheltered = 0
    new_evacuees_expected = 0
    occupancy_rate = 0
    average_occupancy_rate_for_district = 0

    # The start of our loop for our shelters.
    for shelters in range(3):
        user_total_capacity = input("Enter Total Capacity: ")
        total_capacity += user_total_capacity

        user_people_sheltered = input("Enter people sheltered: ")
        people_sheltered += user_people_sheltered

        user_new_evacuees_expected = input("Enter new evacuees expected: ")
        new_evacuees_expected += user_new_evacuees_expected

        occupancy_rate = people_sheltered / total_capacity * PERCENTAGE_RATE
    
    print("*** District Summary ***")
    print("-------------------")
    print("Average occupancy rate: ", (occupancy_rate / 3))
    print("Total sheltered: ", people_sheltered
Total new evacuees expected: 80
Projected occupancy rate: 101.82% 


print("Data collection complete for all districts.")
print("```")



# TODO: Process shelter occupancy data for both districts.

# TODO: For each district, process all shelters.

# TODO: Validate all user input.

# TODO: Calculate and display shelter-level and district-level results.

# TODO: Print a final completion message.