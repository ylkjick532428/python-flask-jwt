import json
import sys
import os
import csv
import codecs

from collections import defaultdict

#===============================================================================
# csv_reader :
#===============================================================================
def csv_reader(filename, fields=[]):
    data = []
    with codecs.open(filename, 'r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tmp = {}
            for j in range(0, len(fields), 1):
                cel = row[j]
                field = fields[j]
                tmp[field] = cel
            data.append(tmp)
            
    return data

#===============================================================================
# covent_rows_to_dict
#===============================================================================
def covent_rows_to_dict(rows, key):
    result = {}
    for row in rows:
        result[key] = row
    return result

def tree(): return defaultdict(tree)

#===============================================================================
# complete_info_back : 补全为空的文明记录信息
#===============================================================================
def complete_info_back(rows):
    pre = rows[0]
    result = tree()
    for row in rows:
        for key, value in row.items():
            if not value:
                row[key] = pre[key]
        
        civilization = row["civilization"]
        continent = row["continent"]
        area = row["area"]
        tmp_key = row["keys"]
        result[civilization][continent][area][tmp_key] = True
        pre = row
        
    return result

#===============================================================================
# complete_info : 补全为空的文明记录信息
#===============================================================================
def complete_info(rows):
    pre = rows[0]
    result = []
    for row in rows:
        for key, value in row.items():
            if not value:
                row[key] = pre[key]
        
        tmp_row = [row[key] for key in ["civilization", "continent", "area", "keys"]]
        result.append(tmp_row)
        pre = row
#     print(result)    
    return result

#===============================================================================
# merge : 数据从后往前合并
# source_data:
#       [['奴隶社会', '亚洲', '古印度', '种姓制度'], 
#       ['奴隶社会', '亚洲', '古印度', '佛教的创立']]
#       合并为
# index_len: 合并的位置, "无印度"位置为3
# return: [['奴隶社会', '亚洲', '古印度', ['种姓制度', '佛教的创立']]      
#===============================================================================
def merge(tmp_source_data, index_len):
    tmp_result = {} #辅助判断数据是否合并
    result = [] # 合并的部分的数据
    tmp_result2 = [] # 未合并部分的数据
    i = -1
    for row in tmp_source_data:
        tmp_key_str = ",".join([row[j] for j in range(0, index_len)])
        if tmp_key_str not in tmp_result:
            tmp_result[tmp_key_str] = []
            tmp_result2.append(row[:index_len])
            result.append([])
            i += 1
        
        tmp = result[i]
        if index_len == 3:
            tmp.append(row[-1])
        else:
            tmp.append({row[-2]:row[-1]})
        result[i] = tmp

    #两部分数据合并
    for i in range(0, len(tmp_result2)):
        row = tmp_result2[i]
        row.append(result[i])
        tmp_result2[i] = row
    
    return tmp_result2

#===============================================================================
# csv2json
#===============================================================================
def csv2json(file_path):
    fields = ["civilization", "continent", "area", "keys"]
    source_data = csv_reader(file_path, fields)
    source_data2 = complete_info(source_data)
#     print (json.dumps(source_data2, ensure_ascii=False, indent=1))
    result = {}
    for i in range(3, -1, -1):
        tmp_fileds = fields[:i]
        source_data2 = merge(source_data2, i)
    return source_data2[0][0][0]



#===============================================================================
# find
#===============================================================================
def find(key):
    global SEARCH_NAME;
    def search_main(data, key, key_path):
        if type(data) == dict:
            for tmp_key, value in data.items():
                tmp_tmp = search_main(value, key, key_path + "." + tmp_key)
            
        elif type(data) == list:
            for tmp_row in data:
                if type(tmp_row) == str:
                    if tmp_row == key:
                        global SEARCH_NAME
                        SEARCH_NAME = key_path[1:] + "." + key
                        return SEARCH_NAME
                else:
                    tmp_tmp = search_main(tmp_row, key, key_path)
        
        else:
            print ("error")
            
    data = csv2json("history.csv")
    print (json.dumps(data, ensure_ascii=False, indent=1))
    key_path = ""
    search_main(data, key, key_path)
    print ("===========================")
    if SEARCH_NAME:
        print (SEARCH_NAME)
    else:
        print ("不存在关键字: %s" % key)
    
if __name__ == '__main__':
    
    key = "汉谟拉比法典"
    find(key)
    
