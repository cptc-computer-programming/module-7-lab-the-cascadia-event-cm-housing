# Lakewood Emergency Operations Center
# Department of Housing

DISTRICT_COUNT = 2
SHELTER_COUNT = 3

MIN_CAPACITY = 1
MIN_PEOPLE_SHELTERED = 1
MIN_NEW_EVACUEES = 0


# Cloverpark intiated variables.
clover_total_capacity = 0
clover_people_sheltered = 0
clover_new_evacuees_expected = 0
clover_occupancy_rate = 0

# Steilacoom intiated variables.
steilacoom_total_capacity = 0
steilacoom_people_sheltered = 0
steilacoom_new_evacuees_expected = 0
steilacoom_occupancy_rate = 0

# The start of our loop over our districts.
for districts in range (2):
    # The start of our loop for our shelters.
    for shelters in range(3):
        user_clover_total_capacity = input("Enter Total Capacity: ")
        clover_total_capacity += user_clover_total_capacity

        user_clover_people_sheltered = input("Enter people sheltered: ")
        clover_people_sheltered += user_clover_people_sheltered

        user_clover_new_evacuees_expected = input("Enter new evacuees expected: ")
        clover_new_evacuees_expected += user_clover_new_evacuees_expected

        clover_occupancy_rate = 

# TODO: Process shelter occupancy data for both districts.

# TODO: For each district, process all shelters.

# TODO: Validate all user input.

# TODO: Calculate and display shelter-level and district-level results.

# TODO: Print a final completion message.