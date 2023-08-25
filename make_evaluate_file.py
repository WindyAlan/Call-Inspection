import pandas as pd
import json

date = '0824'
label_file = r'C:\Users\han.zhang12\Desktop\电销质检\doccano_labeled_data\all_labels_'+date+'.jsonl'
record_file = r'C:\Users\han.zhang12\Desktop\电销质检\0818\20230818_record.xlsx'
output_file = r'C:\Users\han.zhang12\Desktop\电销质检\业务方合规检验文件\业务方合规校验'+date+'.xlsx'


labels_data = []
with open(label_file,'r',encoding='utf-8') as f:
    for line in f.readlines():
        json_dic = json.loads(line)
        if json_dic['label']:
            labels_data.append(json_dic)

left = 1
right = 2000
data = pd.read_excel(record_file)
data = data.loc[data['dialog_id'] >= left]
data = data.loc[data['dialog_id'] <= right]
insert_dialogs = []
for i,dic in data.iterrows():
    dialog = dic['dialog']
    insert_dialogs.append(dialog)

output = []
c = 0
for dic in labels_data:
    id = dic['id']
    text = dic['data']
    label = dic['label']
    if text not in insert_dialogs:
        for l,r,cl in label:
            bad_sent = text[l:r]   
            # 后面吧3改成5
            lst = dic['data'].split('\n')
            orderinfo = json.loads(lst[0])
            employeeinfo = json.loads(lst[1])

            m_text = '\n'.join(lst[5:])
            bad_class = cl
            # print(employeeinfo)
            tmp = {'日期':date,
                   'id':id,
                   'callid':str(orderinfo['callid']),
                   'workNumber':str(employeeinfo['workNumber']),
                   'phone':str(employeeinfo['phone']),
                   'name':str(employeeinfo['name']),
                   'userId':str(employeeinfo['userId']),
                   '对话文本':m_text,
                   '违规句':bad_sent,
                   '违规类型':bad_class}
            output.append(tmp)
    else:
        c += 1

# pd.DataFrame(output).to_csv(r'prac.csv',index=False)
pd.DataFrame(output).to_excel(output_file,index=False)
# print(c)
# print(output[0])