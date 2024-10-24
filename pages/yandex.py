#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

URL = 'https://market.yandex.ru/'
class MainPage(WebPage):

    def __init__(self, web_driver):
        super().__init__(web_driver, URL)

    # Main search field
    search = WebElement(id='header-search')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')
