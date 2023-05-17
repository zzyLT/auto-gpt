from chatGPT import ChatClient
import time
import pandas as pd
import time
# from func_timeout import func_set_timeout
import func_timeout
import calendar
import multiprocessing
import re


OPENAI_EMAIL = "aaaamiaoaaa@gmail.com"
OPENAI_PASSWORD = "daisyZZY0609"
chat = ChatClient(OPENAI_EMAIL, OPENAI_PASSWORD, headless=False, chrome_version=112)



def interact_gpt(text):
    time.sleep(3)
    return chat.interact(text)


if __name__ == '__main__':

    # data = pd.read_csv('./物流职业/extra_post.csv')
    # data = pd.read_csv('answer100.csv')
    data = pd.read_excel('gpt结果汇总1510.xlsx')
    labels = ['职业素养','通用能力','职业技能']
    # for label in labels:
    #     data[label] = None

    for name in list(data['name']):
        for label in labels:
            print(name)
            if str(data.loc[data['name'] == name, label].values[0]) == 'nan':
                demande = '十条'+ name +'最重要的'+ label+'并描述其内容'
                ans = interact_gpt(demande)
                if len(re.findall("：", ans)) < 10:
                    ans = ans + '\n' + interact_gpt('继续')
                data.loc[data['name'] == name, label] = ans
                time.sleep(5)
                print(data.loc[data['name'] == name, label])
                data.to_csv('answer_after_union.csv')
