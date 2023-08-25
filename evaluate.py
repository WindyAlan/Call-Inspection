import pandas as pd
import json

label_file = r'C:\Users\han.zhang12\Desktop\电销质检\doccano_labeled_data\all_labels_0823.jsonl'
record_file = r'C:\Users\han.zhang12\Desktop\电销质检\0817\20230817_record.xlsx'
output_file = r'C:\Users\han.zhang12\Desktop\电销质检\标注质量评估\0823未找出的违规话术.xlsx'


labels_data = []
with open(label_file,'r',encoding='utf-8') as f:
    for line in f.readlines():
        json_dic = json.loads(line)
        if json_dic['label']:
            labels_data.append(json_dic['data'])
# print(labels_data[:2])
# print(len(labels_data))

left = 2001
right = 4000
data = pd.read_excel(record_file)
data = data.loc[data['dialog_id'] >= left]
data = data.loc[data['dialog_id'] <= right]
# print(data)
# exit()

find_count = 0
output = []
for i,dic in data.iterrows():
    dialog = dic['dialog']
    bad = dic['add_bad_case']

    # print(dialog)
    # dialog_lst = dic['dialog'].split('\n')
    # id = dic['sen_id']
    # # print(id,bad)
    # ##################之后要改[dialog_lst[id],bad]
    # dialog_lst[id-1] = ''.join([dialog_lst[id-1],bad])
    # dialog = '\n'.join(dialog_lst)

    if dialog in labels_data:
        # print(dialog,labels_data)
        find_count += 1
    else:
        # print([dialog])
        tmp = {'序号':dic['dialog_id'],'对话内容':dialog,'违规话术':bad}
        output.append(tmp)

pd.DataFrame(output).to_excel(output_file)

print('一共插入{}个不合理话术，找出{}个，占比{:.2f}%。'.format(len(data),find_count,find_count/len(data)))