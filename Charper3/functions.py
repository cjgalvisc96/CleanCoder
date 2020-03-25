# the functions should be small,max 30 lines
# Functions should do one thing. THey should do it well. They should do it only
#  ***** Only one level of abstraction per function ****

def render_page_with_setups_and_theardowns(page_data, is_suite):
    if is_test_page(page_data):
        include_setup_and_teardown_pages(page_data, is_suite)
    return page_data.get_html()

#**** Max three arguments per function****
# if the fucntion have more three aruments you can convert this in objects
make_circle(x, y, radius)
center = Point(0,1)
make_circle(center, radius) # center is aobject type point 

#use try/catch blocks

def delete(page):
    try:
        delete_page_and_all_references(page)
    except Exception as e:
        log_error(e)
    
def delete_page_and_all_references(page):
    delete_page(page)
    registry.delete_reference(page.name)
    config_keys.delete_keys(page.name.make_key())

def log_error(exception):
    logger.log(exception.get_message())