import json

from data_def import Rec
class FileReader:
    def read_data(self) -> list[Rec]:
        pass

class TextReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Rec]:
        f=open(self.path, 'r', encoding='utf-8')
        next(f)
        rec_list:list[Rec]=[]

        for line in f:
            line = line.strip() #delete /n
            data_list=line.split(',')
            rec=Rec(data_list[0],data_list[1],float(data_list[2]),data_list[3])
            rec_list.append(rec)

        f.close()
        return rec_list


class JsonReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Rec]:
        f = open(self.path, 'r', encoding='utf-8')

        rec_list: list[Rec] = []
        for line in f:
            data_dict = json.loads(line)
            rec=Rec(data_dict['date'],data_dict['id'],data_dict['amount'],data_dict['country'])
            rec_list.append(rec)
        f.close()
        return rec_list

if __name__ == '__main__':
    text_reader=TextReader('/Users/laphare/Desktop/project/py/sales_2011_02.txt')
    json_reader= JsonReader('/Users/laphare/Desktop/project/py/sales_2011_03.txt')
    list1=text_reader.read_data()
    list2=json_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)