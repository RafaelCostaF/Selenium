# TODO
# - Change time.sleep -> Wait till load

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
from csv import writer


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


# INITIAL DRIVER SET UP --------------------------------------------------------------------------------------------------------

driver = webdriver.Chrome()

# ENTERING PAGE ----------------------------------------------------------------------------------------------------------------

driver.get("https://play.google.com/console/u/0/developers/9081477095396727508/app-list")

# LOGIN ------------------------------------------------------------------------------------------------------------------------

login = input("Faça o login e pressione enter aqui.\nPressione Enter.")

print("Login realizado.")

# ------------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ == AUTOMATION == ------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------

# Links to access the apps
appLinks = []

# While there's option to go to the next page
while(driver.find_elements_by_class_name("next _ngcontent-ylw-49 _nghost-ylw-31 is-disabled") == []):

    time.sleep(10)

    # Getting links of the apps and appending to the list -------------------------

    links = driver.find_elements_by_tag_name("a")
    numAppsInList = len(driver.find_elements_by_class_name("particle-table-row"))

    for x in range(1,numAppsInList + 1):
        appLinks.append(links[x].get_attribute('href'))
    # -----------------------------------------------------------------------------

    # Try to go to next page
    try:
        driver.find_element_by_xpath("/html/body/div[1]/root/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-list-page/console-section[2]/div/div/console-block-1-column[1]/div/div/console-table/pagination-bar/div/div[2]/div[2]/div[2]/material-button[3]/material-ripple").click()
    except:
        # Get out of the loop
        break

print(len(appLinks))
# Collecting data from the apps --------------------------------------------------

listApps = []
for link in appLinks:
    driver.get(link)
    time.sleep(5)
    name = driver.find_elements_by_tag_name("span")[75].text
    activeUsers = driver.find_elements_by_tag_name("span")[78].text.split(" ")[0]
    listApps.append(name)
    listApps.append(activeUsers)
    append_list_as_row('googleConsoleApps.csv', listApps)
    listApps = []
    # print("------------------------------------------")
    # # Name of the app
    # print("- - - - "+name+" - - - -")
    # # Number of active users
    # print(activeUsers)
    # print("------------------------------------------")

# --------------------------------------------------------------------------------



# Closing driver and quitting webpage --------------------------------------------

driver.close()
driver.quit()

# End ----------------------------------------------------------------------------