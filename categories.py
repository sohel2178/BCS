from base import (openbrowser,closebrowser,base_url,
browser,get_total_page,
get_questions_per_page,save_categorize_questions,get_options,save_output_with_options)

import helper

import time

import json


# data = {}
# data['categories'] = []

save_output_with_options('./output/categories-Math.json')

# with open('./output/test.json','r+') as f:
#     data = json.load(f)
#     questions = data['questions']

#     for question in questions:
#         question['options'] = get_options(question['options_url'])



# for i,category in enumerate(get_categories()):
#     if i==8:
#         save_categorize_questions(category)



browser.close()




# q_list_per_page = get_questions_per_page('https://www.bcsprep.com/questionsincategory.php?catid=1',1)

# closebrowser()

# print(q_list_per_page)




# categories = get_categories()

# print(categories)

# for cat in get_categories():
#     category = {}
#     category['url'] = cat
#     category['total_page'] = get_total_page(cat)
#     data['categories'].append(category)

# with open('./output/categories.json', 'w') as outfile:  
#     json.dump(data, outfile,indent=4)




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






