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

# Variables have a context

class GuessStaticsMessage:
    number = 0
    verb = ''
    plural_modifier = ''

    def make(candidate, count):
        create_plural_dependt_message_parts(count)
        return f"There {verb}, {number}, {candidate}, {plural_modifier}"
    
    def create_plural_dependt_message_parts(count):
        if count == 0:
            there_are_not_letters()
        elif count == 1:
            there_is_one_letter()
        else:
            there_are_many_letters(count)
    
    def there_are_many_letters(count):
        number = str(count)
        verb = "are"
        plural_modifier = 's'

    def there_is_one_letter(count):
        number = '1'
        verb = 'is'
        plural_modifier=''

    def there_are_not_letters(count):
        number = 'no'
        verb = 'are'
        plural_modifier='s'