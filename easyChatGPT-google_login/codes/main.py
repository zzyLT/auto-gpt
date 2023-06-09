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


OPENAI_EMAIL = "zuzhuangyan@gmail.com"#"aaaamiaoaaa@gmail.com"
OPENAI_PASSWORD = "daisyZZY0609"
chat = ChatClient(OPENAI_EMAIL, OPENAI_PASSWORD, headless=False, chrome_version=113)



def interact_gpt(text):
    time.sleep(3)
    return chat.interact(text)


if __name__ == '__main__':

    """
    三个维度合并到一起提问
    """
<<<<<<< HEAD
    data = pd.read_csv('../examples/物流职业/40names.csv')
    data['answer'] = np.NAN

    # data = pd.read_csv('../result/answer_detail.csv')
=======
    data = pd.read_csv('../examples/rework_names.csv')
    data['answer'] = np.NAN

    # data = pd.read_csv('../examples/answer_40posts_05-31.csv')
>>>>>>> parent of cf09553 (40 jobs result plus detail)

    time.sleep(30)
    for name in list(data['name']):
            print('>> ', name)
            if str(data.loc[data['name'] == name, 'answer'].values[0]) == 'nan':
                # demande = '十二条'+ name + '岗位' +'最重要的'+ label+'并描述其内容'
                demande = '接下来你将充当物流行业的职业分析师，配合我完成一系列文本分析任务，要求：' \
<<<<<<< HEAD
                         f'针对{name}，从专业知识、技术能力、沟通能力、管理能力、自我学习能力五个维度进行分析：' \
                          f'每个维度拓展提取并分条列出不少于十条重要能力，每条能力说明需要提供10个技能关键词，并不需要描述性语句。' \
=======
                         f'针对{name}，从专业素养、通用能力、专业技能三个维度进行分析，每个维度提取并分条列出不少于十条重要能力，每条能力说明需要提供10个技能关键词，并不需要描述性语句。' \
>>>>>>> parent of cf09553 (40 jobs result plus detail)
                          f'每个重要能力的名称需严格遵守格式要求即“XXX能力”，' \
                          f'并且能力名称不超过10个中文字符。' \
                          f'同时，每条能力的技能关键词要求用中文顿号隔开，并且每两个顿号之间为完整的技能关键词，并且每个技能关键词长度严格限定在4-6个中文字符之间。'
                ans = interact_gpt(demande)
                # ans = ans + '\n' + interact_gpt('继续')
                data.loc[data['name'] == name, 'answer'] = ans
                time.sleep(5)
                print(data.loc[data['name'] == name, 'answer'])
<<<<<<< HEAD
                data.to_csv('../result/answer_5cap.csv', index=False)
=======
                data.to_csv('../result/answer_rework.csv', index=False)
>>>>>>> parent of cf09553 (40 jobs result plus detail)
    exit()


    """
    三个维度逐个提问
    """
    # data = pd.read_csv('./物流职业/extra_post.csv')
    # data = pd.read_csv('answer100.csv')
    # data = pd.read_excel('gpt结果汇总1510.xlsx')
    data = pd.read_csv('../examples/answer_after_union.csv')
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
