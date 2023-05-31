import numpy as np

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

    """
    三个维度合并到一起提问
    """
    data = pd.read_csv('./物流职业/40names.csv')
    data['answer'] = np.NAN

    time.sleep(10)
    for name in list(data['name']):
            print('>> ', name)
            if str(data.loc[data['name'] == name, 'answer'].values[0]) == 'nan':
                # demande = '十二条'+ name + '岗位' +'最重要的'+ label+'并描述其内容'
                demande = '接下来你将充当物流行业的职业分析师，配合我完成一系列文本分析任务，要求：' \
                         f'针对{name}，从专业素养、通用能力、专业技能三个维度进行分析，每个维度提取十条重要能力，每条能力说明需要提供一定数量的技能关键词。每个重要能力的名称需严格遵守格式要求即“XXX能力”' \
                          f'每个重要能力的名称需严格遵守格式要求即“XXX能力”，每条能力的技能关键词要求用中文顿号隔开，并且每两个顿号之间为完整的技能关键词。'
                ans = interact_gpt(demande)
                ans = ans + '\n' + interact_gpt('继续')
                data.loc[data['name'] == name, 'answer'] = ans
                time.sleep(5)
                print(data.loc[data['name'] == name, 'answer'])
                data.to_csv('answer_40posts_05-31.csv', index=False)
    exit()


    """
    三个维度逐个提问
    """
    # data = pd.read_csv('./物流职业/extra_post.csv')
    # data = pd.read_csv('answer100.csv')
    # data = pd.read_excel('gpt结果汇总1510.xlsx')
    data = pd.read_csv('answer_after_union.csv')
    labels = ['职业素养','通用能力','职业技能']
    # for label in labels:
    #     data[label] = None

    time.sleep(30)
    for name in list(data['name']):
        for label in labels:
            print(name)
            if str(data.loc[data['name'] == name, label].values[0]) == 'nan':
                # demande = '十二条'+ name + '岗位' +'最重要的'+ label+'并描述其内容'
                ans = interact_gpt(demande)
                if len(re.findall("：", ans)) < 11:
                    ans = ans + '\n' + interact_gpt('继续')
                data.loc[data['name'] == name, label] = ans
                time.sleep(5)
                print(data.loc[data['name'] == name, label])
                data.to_csv('answer_after_union.csv', index=False)
