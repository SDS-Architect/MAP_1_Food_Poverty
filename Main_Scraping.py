### Import Libs
import pandas
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

### Importing from other files
from supermarket_parameters import (
    supermarket_parameters,
    supermarket_list,
    product_list,
    path_chrome,
)
from General_Utilities import slow_typing

### Main Function
def supermarket_sweeper(supermarkets, products, supermarket_parameters):

    ### Set up main list
    main_product_list = []
    main_price_list = []

    ### Set up back up list
    reserve_product_list = []
    reserve_price_list = []

    ### Set up a loop
    driver = webdriver.Chrome(executable_path=path_chrome)

    # Take a supermarket
    for supermarket_name in supermarkets:

        # Take a product
        for product_name in products:

            ### Get page
            driver.get(supermarket_parameters[supermarket_name]["home_url_id"])

            ### Slow down speed for memory
            time.sleep(2)

            ### Find the search box
            element = driver.find_element_by_css_selector(
                supermarket_parameters[supermarket_name]["search_bar_id"]
            )

            element.click()

            ### Type in name of product
            slow_typing(element, product_name)

            ### Find the button to search
            submit_button = driver.find_element_by_css_selector(
                supermarket_parameters[supermarket_name]["search_button_path"]
            )

            ### Search
            submit_button.click()

            ### Pause for memory
            time.sleep(5)

            ### Click on organise by cheapest

            ### Asda version
            if supermarket_name == "Asda":

                ### Pause
                time.sleep(1)

                ### Find the select button
                sort_opt = driver.find_element_by_css_selector(
                    supermarket_parameters["Asda"]["css_id_organise"]
                )

                ### Click button
                sort_opt.click()

                ### Pause
                time.sleep(3)

                ### Find the lowest price button
                select_opt = driver.find_elements_by_css_selector(
                    supermarket_parameters["Asda"]["css_option_text"]
                )

                ### Click the button
                select_opt[1].click()

                ### Sleep
                time.sleep(1)
                driver.find_element_by_css_selector(
                    supermarket_parameters["Asda"]["footer_button"]
                ).click()

            ### Handling standard methods
            else:
                el = driver.find_element_by_css_selector(
                    supermarket_parameters[supermarket_name]["css_id_organise"]
                )
                for option in el.find_elements_by_tag_name("option"):
                    if (
                        option.text
                        == supermarket_parameters[supermarket_name]["css_option_text"]
                    ):
                        option.click()
                        break

            ### Pause for memory
            time.sleep(5)

            # Turn into Beautiful Soup
            soup = BeautifulSoup(driver.page_source, "html.parser")

            ### Modify For Morrisons Sidebar issue:
            if supermarket_name == "Morrisons":
                soup = soup.find(
                    supermarket_parameters["Morrisons"]["main_area_class"],
                    {"class": supermarket_parameters["Morrisons"]["main_area_name"]},
                )

            ### Extract product name
            main_prod = soup.find_all(
                supermarket_parameters[supermarket_name]["prod_name_type"],
                {"class": supermarket_parameters[supermarket_name]["prod_name_class"]},
            )[0]["alt"]

            ### Extract back up product name
            rese_prod = soup.find_all(
                supermarket_parameters[supermarket_name]["prod_name_type"],
                {"class": supermarket_parameters[supermarket_name]["prod_name_class"]},
            )[1]["alt"]

            ## Extract prices
            main_price = soup.find_all(
                supermarket_parameters[supermarket_name]["prod_price_type"],
                {"class": supermarket_parameters[supermarket_name]["prod_price_class"]},
            )[0].text

            rese_price = soup.find_all(
                supermarket_parameters[supermarket_name]["prod_price_type"],
                {"class": supermarket_parameters[supermarket_name]["prod_price_class"]},
            )[1].text

            if supermarket_name == "Tesco":
                main_price = soup.find_all(
                    supermarket_parameters[supermarket_name]["prod_price_type"],
                    {
                        "class": supermarket_parameters[supermarket_name][
                            "prod_price_class"
                        ]
                    },
                )[0].text

                rese_price = soup.find_all(
                    supermarket_parameters[supermarket_name]["prod_price_type"],
                    {
                        "class": supermarket_parameters[supermarket_name][
                            "prod_price_class"
                        ]
                    },
                )[2].text

            ### Appending all to lists
            main_product_list.append(main_prod)

            reserve_product_list.append(rese_prod)

            main_price_list.append(main_price)

            reserve_price_list.append(rese_price)

    return (
        main_product_list,
        reserve_product_list,
        main_price_list,
        reserve_price_list,
    )
