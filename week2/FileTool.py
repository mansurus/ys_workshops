import csv
import json
from pathlib import Path
import pandas as pd


class FileTool:
    
    def __init__(self,path,fields:list):
        self.path=path
        self.fields=fields
        while True:
            menu = """
            To create a new csv file: "N"
            To view an existing csv file: "R"
            To search in a csv file: "S"
            To merge csv files: "M"
            To json file: "J"
            To quit: "Q"       
        """
            print(menu)
            operation = input("Please enter a key:").lower()
            if operation=="n":
                self.write()
            elif operation=="r":
                self.read()
            elif operation=="s":
                self.search()
            elif operation=="m":
                self.merge()
            elif operation=="j":
                self.toJson()
            elif operation=="q":
                return None
            else:
                print('\x1b[0;30;41m' + 'Please enter a valid key!' + '\x1b[0m')

    def read(self):
        with open(self.path, 'r') as csv_file:
            csv_reader=csv.reader(csv_file)

            for line in csv_reader:
                print(line)
    
    def write(self):
        answer=input("Do you want to write field names? Y/N: ").lower()
        if answer=="y":
             fieldNames = input("Please enter field names with one space apart: ").lower()
             newList = fieldNames.split(" ")
             self.fields = newList
             fieldLen = len(newList)
             tempList = []
             for i in range(fieldLen):
                 data = input("Please enter data: ")
                 tempList.append(data)
             rows = []
             rows.append(tempList)
             with open('new.csv', 'w', encoding='UTF8', newline='') as new_csv:
                writer = csv.writer(new_csv)
                writer.writerow(self.fields)
                writer.writerows(rows)
        elif answer=="n":
             colLen = int(input("Please enter number of fields: "))
             tempList = []
             for i in range(colLen):
                 data = input("Please enter data: ")
                 tempList.append(data)
             rows = []
             rows.append(tempList)
             with open('new.csv', 'w', encoding='UTF8', newline='') as new_csv:
                writer = csv.writer(new_csv)
                writer.writerows(rows)
        else:
            print('\x1b[0;30;41m' + 'Please enter a valid key!' + '\x1b[0m')
            self.write()
    def merge(self):
        df = pd.concat(
            map(pd.read_csv, ['addresses.csv', 'addresses copy.csv']), ignore_index=True)
        print(df)
        
    def toJson(self):
        data = {}
        with open(self.path, 'r') as csv_file:
            csv_reader=csv.DictReader(csv_file)
            for line in csv_reader:
                data = line
        with open("new.json",'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))
    
    def search(self):
        keyword = str(input("Please enter a search keyword: "))
        with open(self.path, 'r') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if keyword.lower() in row[0].lower(): #looks for first field only
                    print(row)
                

p = FileTool("addresses.csv",["a","b","c"])
    