import numpy as np

from codes.chatGPT import ChatClient
import time
import pandas as pd
import time
# from func_timeout import func_set_timeout
# import func_timeout
import calendar
import multiprocessing
import re


OPENAI_EMAIL = "aaaamiaoaaa@gmail.com"#"zuzhuangyan@gmail.com"#TODO !!!!!!!!!!!!!!!!!!!!
OPENAI_PASSWORD = "daisyZZY0609" #TODO !!!!!!!!!!!!!!!!!!!!
chat = ChatClient(OPENAI_EMAIL, OPENAI_PASSWORD, headless=False, chrome_version=114)



def interact_gpt(text):
    time.sleep(3)
    return chat.interact(text)


if __name__ == '__main__':

    """
    三个维度合并到一起提问
    """
    # data = pd.read_excel('713 职业名称.xlsx')
    data = pd.read_csv('extra.csv')
    data['answer'] = np.NAN

    min = 0
    max = 999

    # data = pd.read_csv(f'./result/answer_{min}_{max}.csv')

    time.sleep(30)
    list_name = list(data['职业名称'])

    for i in range(len(list_name)):
        if i >= min and i < max :
            name = list_name[i]
            print('>> ', name)
            if str(data.loc[data['职业名称'] == name, 'answer'].values[0]) == 'nan':
                # demande = '十二条'+ name + '岗位' +'最重要的'+ label+'并描述其内容'
                demande = '接下来你将充当物流行业的职业分析师，配合我完成一系列文本分析任务，要求：' \
                         f'针对{name}岗位，从专业素养、通用能力、专业技能三个维度进行分析，每个维度提取并分条列出不少于十条重要能力，每条能力说明需要提供10个技能关键词，并不需要描述性语句。' \
                          f'每个重要能力的名称需严格遵守格式要求即“XXX能力”，' \
                          f'并且能力名称不超过10个中文字符。' \
                          f'同时，每条能力的技能关键词要求用中文顿号隔开，并且每两个顿号之间为完整的技能关键词，并且每个技能关键词长度严格限定在4-6个中文字符之间。'

                ans = interact_gpt(demande)
                # ans = ans + '\n' + interact_gpt('继续')
                data.loc[data['职业名称'] == name, 'answer'] = ans
                time.sleep(5)
                print(data.loc[data['职业名称'] == name, 'answer'])
                data.to_csv(f'./result/answer_{min}_{max}.csv', index=False)
