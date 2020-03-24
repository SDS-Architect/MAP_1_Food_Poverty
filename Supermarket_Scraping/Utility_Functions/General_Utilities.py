### Import Libs
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def slow_typing(element, text):
    """ One-click opening and loading of file.
    
    Parameters
    ----------
    element: string
        A string that represents an html element (usually a product)
    
    Returns
    -------
    
    Nothing.
        Action based function.
    """
    for character in text:
        element.send_keys(character)
        time.sleep(0.2)


def read_products(file_name, test_mode = False):
    ''' Designed to read in a csv file of generic product names. MUST 
        use 'Products' as column name. 
    
    Parameters
    ----------
    file: string
        A string that represents a path to a csv file.
    
    Returns
    -------
    product_list: list 
        A list of generic product names for further processing. 

    '''

    ### Checking for blank file and test mode

    if file_name == None and test_mode == True:
        try:
            working_file = pd.read_csv('test_scrape.csv')

            product_list = list(working_file['Products'].values)

            return(product_list)

        except:
            print("Cannot find test file, check it's there!")

    else:
        working_file = pd.read_csv(file_name)

        product_list = list(working_file['Products'].values)

        return(product_list)

            


        






