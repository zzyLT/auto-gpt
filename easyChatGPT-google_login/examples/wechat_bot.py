from chatGPT import ChatClient
import time
import pandas as pd
import time
# from func_timeout import func_set_timeout
import func_timeout
import calendar
import multiprocessing

# path = "E:/nos\灯塔工厂\按八大能力分析\GPT/0______ChatGPT_result_1680858959.xlsx"
# data = pd.read_excel(path)
# print(data)

OPENAI_EMAIL = "aaaamiaoaaa@gmail.com"
OPENAI_PASSWORD = "daisyZZY0609"
chat = ChatClient(OPENAI_EMAIL, OPENAI_PASSWORD, headless=False, chrome_version=112)



def interact_gpt(text):
    time.sleep(3)
    return chat.interact(text)

# def funct(start, end):
#     for index,row in data.iterrows():
#         if (row['education'] == '大专') or (row['education'] == '本科') or (row['education'] == '硕士'):
#             print("********************" + str(index) + ":" + str(len(data)) + "********************")
#             if (index >= start) and (index < end) and (str(row['summary']) == "nan"):
#                 try:
#                     try:
#                         description = data['job_info'][index]
#                         answer = interact_gpt(demande + description)
#                         data["summary"][index] = answer
#                         print(answer)
#                         data.to_csv("E:\\nos\灯塔工厂\按八大能力分析\\GPT\\"+ str(start) +"______ChatGPT_result_" + str(calendar.timegm(time.gmtime())) + ".csv")
#                     except func_timeout.exceptions.FunctionTimedOut as e:
#                         print(e)
#                 except Exception as e:
#                     print("error:  ", e)
#                 time.sleep(30)


# def process(num = [0,-1], len = len(data)):
#     if num[1] == -1:
#         num[1] = len
#     process0 = multiprocessing.Process(target=funct,kwargs={"start": num[0],"end":num[1]})
#     process0.start()

if __name__ == '__main__':
    # target：指定执行的函数名
    # args:使用元组方式给指定任务传参
    # kwargs:使用字典方式给指定任务传参

    # i = True
    # for num in [[0,-1]]: #100],[101,200],[201,


    # process()

    # time.sleep(5)
    # funct(0, len(data))


    # data = pd.read_csv('./物流职业/extra_post.csv')
    data = pd.read_csv('answer100.csv')
    labels = ['职业素养','通用能力','职业技能']
    # for label in labels:
    #     data[label] = None

    for name in list(data['name']):
        for label in labels:
            if str(data.loc[data['name'] == name, label].values[0]) == 'nan':
                demande = '十条'+ name +'最重要的'+ label+'并描述其内容'
                ans = interact_gpt(demande)
                data.loc[data['name'] == name, label] = ans + '\n' + interact_gpt('继续')
                time.sleep(5)
                print(data.loc[data['name'] == name, label])
                data.to_csv('answer100.csv')
