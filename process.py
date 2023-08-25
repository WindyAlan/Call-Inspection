import json
from collections import defaultdict
import pandas as pd
#挑选除了未提及的不合理话术
bad_case = {}
# print(bad_case,type(bad_case))

# with open('all.jsonl','r',encoding='utf-8') as f:
#     for json_str in f.readlines():
#         dic = json.loads(json_str)
#         label = dic['label']
#         sent = dic['data']
#         if not label or label == [[8, 13, "功能未提及"]]:
#             continue
#         # print(label)
#         for lst in label:
#             l,r,cl = tuple(lst)
#             bad_case[cl] = bad_case.get(cl,[])
#             bad_case[cl].append(sent[l:r])
#             # bad_case.append([sent[l:r],cl])
# print(bad_case)
# with open('bad_case.json','w',encoding='utf-8') as f:
#     json.dump(bad_case,f,indent=4,ensure_ascii=False)
        

# exps = {'未告知如何关闭':'不想用.{0,10}关[掉闭了]',
#         '传输负面信息':'悬浮窗.{0,10}不好用?|悬浮窗.{0,10}没有.{0,5}货源?',
#         '威胁恐吓司机':'不开这个功能.{0,10}账号.{0,10}(不[能用可]|黑名单|处理不了)|不开这个功能.{0,10}货源?',
#         '虚假承诺':'(只要)?.{0,10}悬浮窗.{0,10}(高价货源|(运费)?.{0,5}高.{0,5}货源?|(所有|完全|全部|都)).{0,5}|(完全|精准|精确|准确|优先)匹配.{0,5}|[不无没].{0,10}[假坏差]货?',
#         '沟通态度恶劣':'神经病|妈的',
#         }


with open('20230810_label_data.json','r',encoding='utf-8') as f:
    data = json.load(f)
# print(data)
# data = pd.DataFrame(data)
# data.to_excel('20230810_label_data.xlsx')
new_data = []
for dic in data:
    tmp = {}
    # print(dic)
    for k in dic.keys():
        if k == 'text':
            tmp[k] = dic[k]
        else:
            # print(dic[k])
            for k2 in dic[k].keys():
                # print(k2)
                tmp[k2] = dic[k][k2]
    # print(tmp)
    new_data.append(tmp)
print(new_data)
new_data = pd.DataFrame(new_data)
new_data .to_excel('20230810_label_data.xlsx')