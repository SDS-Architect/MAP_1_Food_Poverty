### Path to Chromium
path_chrome = "/home/son-of-skynet/Downloads/chromedriver"

### List Supermarkets
supermarket_list = ["Tesco", "Morrisons", "Asda"]

### Product List
product_list = ["Mince", "Orange"]

### Listing Parameters
supermarket_parameters = {
    "Tesco": {
        "home_url_id": "https://www.tesco.com/groceries/en-GB/",
        "search_bar_id": ".search-bar__input",
        "search_button_path": ".search-bar button.search-bar__submit",
        "prod_name_type": "img",
        "prod_name_class": "product-image",
        "prod_price_type": "span",
        "prod_price_class": "value",
        "css_id_organise": ".sort-and-filter .sort-control-container",
        "css_option_text": "Price: Low to High",
    },
    "Asda": {
        "home_url_id": "https://groceries.asda.com/",
        "search_bar_id": ".search-form__input",
        "search_button_path": ".search-form__search-button",
        "prod_name_type": "img",
        "prod_name_class": "co-product__image co-item__image",
        "prod_price_type": "strong",
        "prod_price_class": "co-product__price",
        "css_id_organise": ".asda-filter",
        "css_option_text": ".asda-radio-button__label",
        "footer_button": ".asda-dropdown-menu__footer",
    },
    "Morrisons": {
        "home_url_id": "https://groceries.morrisons.com/webshop/startWebshop.do",
        "search_bar_id": "#findText",
        "search_button_path": "#findButton",
        "prod_name_type": "img",
        "prod_name_class": "fop-img",
        "prod_price_type": "span",
        "prod_price_class": "fop-price",
        "main_area_class": "div",
        "main_area_name": "main-column",
        "css_id_organise": ".sort-wrapper",
        "css_option_text": "Total price: Low to High"
    },
    "Iceland":{
        "home_url_id": "https://www.iceland.co.uk/",
        "search_bar_id": "#header-search",
        "search_button_path": ".btn-dark",
        "prod_name_type": "img",
        "prod_name_class": "thumb-link",
        "prod_price_type": "",
        "prod_price_class": "",
        "main_area_class": "",
        "main_area_name": "",
        "css_id_organise": "",
        "css_option_text": ""
    }
}
