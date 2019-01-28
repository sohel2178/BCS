from selenium import webdriver

from os import path

import json

import time

import helper

base_url = 'https://www.bcsprep.com/categories.php'

browser = webdriver.Chrome(r'C:\Users\sohel\Desktop\Selenium\chromedriver.exe')
# browser = webdriver.Firefox()

total_page = 10

data = {}

data['answers'] = []



def openbrowser(url):
    browser.get(url)

def closebrowser():
    browser.close()


def get_total_page(url):
    browser.get(url)

    paginator = browser.find_element_by_class_name('pagination')

    pages = paginator.find_elements_by_tag_name('li')

    last_page = pages[-2]

    lhref = last_page.find_element_by_tag_name('a')

    return lhref.text


def save_output_with_options(file_path):
    q_list = helper.get_all_questions(file_path)

    data ={}
    data['questions'] =[]

    for question in q_list:
        question['options'] = get_options(question['options_url'])
        data['questions'].append(question)

    (file_name,exten) = path.splitext(file_path)
    out_file = file_name+"-final"+exten

    with open(out_file, 'w') as outfile:  
        json.dump(data, outfile,indent=4)



        



def get_questions_per_page(root_url,page_number):
    url = root_url+"&page="+str(page_number)
    browser.get(url)
    # (browser.page_source).encode('ascii', 'ignore')
    # (browser.page_source).encode('utf-8')

    question_list=[]

    question_container = browser.find_element_by_xpath('/html/body/div[2]/table/tbody')

    question_sections = question_container.find_elements_by_tag_name('tr')

    for section in question_sections:

        question = {}
        for i,td in enumerate(section.find_elements_by_tag_name('td')):
            if i==0:
                question['question']=td.text
            elif i==1:
                question['answer']=td.text
            elif i==2:
                question['options_url']=td.find_element_by_tag_name('a').get_attribute('href')

        question_list.append(question)
    
    return question_list
            
            




    # lastpage=paginator.find_element_by_xpath('/html/body/div[2]/ul[2]/li[-1]/a')
    # print(lastpage.text)


def save_categorize_questions(category):
    url = category['url']
    subject = category['subject']
    total_page = category['total_page']

    qs ={}

    qs['questions'] =[]

    for page in range(int(total_page)):
        qs['questions'].extend(get_questions_per_page(url,page+1))

    
    with open('./output/categories-'+subject+'.json', 'w') as outfile:  
        json.dump(qs, outfile,indent=4)

def get_options(url):
    browser.get(url)

    options_container = browser.find_elements_by_class_name('radio')

    options = []

    for option_container in options_container:
        option = option_container.find_element_by_tag_name('label').text
        options.append(option)

    return options

def print_answer_per_page(page_number,subject_name):

    url = base_url+"/"+subject_name+"/"+page_number

    browser.get(url)
    time.sleep(3)

    answers =browser.find_elements_by_class_name('answer')

    print(len(answers))

    for answer in answers:
        answer.click()
        time.sleep(1)

    actual_answers = browser.find_elements_by_class_name("jq-hdnakqb")


    for answer in actual_answers:
        while answer.text=='':
            continue
        data['answers'].append(answer.text)



def get_all_answer_of_a_section(subject_name,section_range):
    for i in section_range:
        first_section = "{0:0>3}".format(i)

        for i in range(total_page):
            second_section = "{0:0>3}".format(i+1)
            page_number = first_section+second_section

            print(page_number)
            print_answer_per_page(page_number,subject_name)

            # time.sleep(20)

    browser.close()

    with open('../../output_data/'+subject_name+'-answers.json', 'w') as outfile:  
        json.dump(data, outfile,indent=4)