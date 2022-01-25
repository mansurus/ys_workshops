import argparse
import TableOperationsController

parser = argparse.ArgumentParser()
parser.add_argument("--dbName", "--db", type=str)
parser.add_argument("--jsonFile", "--file", type=str)
args = parser.parse_args()

dbName = args.dbName
jsonFile = args.jsonFile

table = TableOperationsController.TableCreate()
table.Insertion(dbName,jsonFile)
