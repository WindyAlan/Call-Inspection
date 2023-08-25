import os 
import random
import json
import pandas as pd


base_cases_str = '悬浮窗这个功能确实不好用，你开一下再关掉吧\n\
悬浮窗这个功能里面没有什么货源，你帮忙开一下，不想用就关掉\n\
如果不开这个功能的话，后期这个账号就不能使用了\n\
如果不开这个功能的话，后期这个账号就不用登录不了\n\
如果不开这个功能的话，后期这个账号被会被拉入黑名单\n\
如果不开这个功能的话，后期这个账号遇到问题，处理不了的\n\
如果不开这个功能的话，货源质量无法保障\n\
现在货源质量有好有差，不开这个功能，就找不到高价货源\n\
不开这个功能，后期就不会向您推送货源\n\
不开这个功能，后期就不会向您高价货源\n\
只要打开悬浮窗，平台就会给你推送高价货源\n\
只要打开悬浮窗，我这边后台登记一下，然后给您推送高价货源\n\
只要开启悬浮窗，后面会给你推送运费更高的货源\n\
悬浮窗里面推送的货源都是运费高的好货\n\
只要开启悬浮窗，里面平台的所有货源都能看到\n\
只要开启悬浮窗，平台所有货源都能抢，像一些高等级货源也同样能抢\n\
这个功能后期给您推送的货源都是完全匹配您车辆和需求的货源\n\
这个功能可以给你精准匹配货源，不会出现假货之类的\n\
神经病\n\
脑子有问题\n\
他妈的'

# print(base_cases_str.split('\n'))

bad_cases = base_cases_str.split('\n')
dir_name = os.path.dirname(__file__)
date = '0821'
file_name = os.path.join(dir_name,os.path.join(date,'2023'+date+'.jsonl'))
output_file = os.path.join(dir_name,os.path.join(date,'2023'+date+'_modify.jsonl'))
record_file = os.path.join(dir_name,os.path.join(date,'2023'+date+'_record.xlsx'))

# print(file_name,output_file,record_file)

raw = []
with open(file_name,'r',encoding='utf-8') as f:
    for line in f.readlines():
        dic = json.loads(line)
        raw.append(dic)

ids = [i for i in range(len(raw))]

# 2%
select_ids = random.sample(ids,2 * len(raw)//100)
# print(bad_cases)
# print(2 * len(raw)//100)

record = []
insert_bad = []
for id in select_ids:
    modify_dic = raw[id]
    texts = modify_dic['text'].split('\n')
    bad = random.sample(bad_cases,1)[0]
    sen_id = random.sample(list(range(5,len(texts))),1)[0]

    insert_bad.append(bad)

    texts[sen_id] = ''.join([texts[sen_id],bad])
    modify_dic['text'] = '\n'.join(texts)

    record.append({'dialog_id':id+1,'dialog':modify_dic['text'],'sen_id':sen_id,'add_bad_case':bad})

# print(raw)
# print(select_ids,len(select_ids))
print(insert_bad)

record = sorted(record,key=lambda x:x['dialog_id'])

with open(output_file,'w',encoding='utf-8') as f:
    for j in raw:
        f.write(json.dumps(j,ensure_ascii=False))
        f.write('\n')

pd.DataFrame(record).to_excel(record_file,index=False)
print('done!')

