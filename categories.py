from base import openbrowser,closebrowser,base_url,browser,get_total_page

from helper import get_categories

import time

import json


data = {}
data['categories'] = []

# categories = get_categories()

# print(categories)

for cat in get_categories():
    print(get_total_page(cat))




# total_page = get_total_page('https://www.bcsprep.com/questionsincategory.php?catid=2')
# print(total_page)

# openbrowser(base_url)

# maincontainer =browser.find_element_by_class_name('container')

# elements = maincontainer.find_elements_by_xpath('//a[@href]')

# for element in elements:
#     if element.text == 'Read All Questions':
#         data['categories'].append(element.get_attribute("href"))

# time.sleep(2)

# with open('./output/categories.json', 'w') as outfile:  
#     json.dump(data, outfile,indent=4)



closebrowser()


