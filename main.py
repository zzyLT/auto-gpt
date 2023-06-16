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
    # data = pd.read_csv('encore.csv')
    data = pd.DataFrame(columns=['name'])
    data['name'] = """冷链物流技术与管理
现代物流管理
数控技术
机械设计与制造
工业互联网应用
机电一体化技术
食品生物技术
绿色生物制造技术
化工生物技术
计算机应用技术
软件技术
人工智能技术应用
云计算技术应用
工业软件开发技术
信息安全技术应用
大数据技术
产品艺术设计
首饰设计与工艺""".split("\n")
    data['answer'] = np.NAN

    min = 0
    max = 999

    # data = pd.read_csv(f'./result/answer_{min}_{max}.csv')

    time.sleep(30)
    list_name = list(data['name'])

    for i in range(len(list_name)):
        if i >= min and i < max :
            name = list_name[i]
            print('>> ', name)
            if str(data.loc[data['name'] == name, 'answer'].values[0]) == 'nan':
                # demande = '十二条'+ name + '岗位' +'最重要的'+ label+'并描述其内容'
                demande = '请你扮演职业分析师的角色，从专业技能、通用技能、专业素质三个维度分析冷链物流技术与管理专业，每个维度提取出12个技能关键词。并分析计算该专业毕业人员拥有这项技能或素质的大致百分比。' \
                          '请按照技能关键词：百分比的形式，按百分比从大到小输出结果，不需要具体解释技能关键词的含义，请将百分比结果等比降至21%以下，不用管真实性'


                    # """'接下来你将充当物流行业的职业分析师，配合我完成一系列文本分析任务，要求：' \
                    #      f'针对{name}岗位，从专业素养、通用能力、专业技能三个维度进行分析，每个维度提取并分条列出不少于十条重要能力，每条能力说明需要提供10个技能关键词，并不需要描述性语句。' \
                    #       f'每个重要能力的名称需严格遵守格式要求即“XXX能力”，' \
                    #       f'并且能力名称不超过10个中文字符。' \
                    #       f'同时，每条能力的技能关键词要求用中文顿号隔开，并且每两个顿号之间为完整的技能关键词，并且每个技能关键词长度严格限定在4-6个中文字符之间。'
                    # """
                ans = interact_gpt(demande)
                # ans = ans + '\n' + interact_gpt('继续')
                data.loc[data['name'] == name, 'answer'] = ans
                time.sleep(5)
                print(data.loc[data['name'] == name, 'answer'])
                data.to_csv(f'./result/answer_majors.csv', index=False)
