# Only syntaxis samples

# The importante of meaning names
def get_flagged_cells(gameboard):
    flagged_cells = []
    for cell in gameboard:
        if cell.is_flagged():
            flagged_cells.add(cell)
    return flagged_cells


# Use searcheable names

real_days_per_ideal_day = 4
WORK_DAYS_PER_WEEK = 5
_sum = 0
for j in range(NUMBER_OF_TASKS):
    real_task_days = task_estimate[j] * real_days_per_ideal_day
    real_task_weeks = (real_days / WORK_DAYS_PER_WEEK)
    _sum += real_task_weeks


# Class names (a class name should not be a verb)
"""
    class Manager()
    class Processor()
    class Data()
    class INfo()
"""
# Methods Names (Methods should have verb or verb phrase names)
name = employee.get_name()
customer.set_name("Mike")
if paycheck.is_posted(): ...