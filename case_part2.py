import xlrd
from datetime import datetime
import csv

def main():
    data = xlrd.open_workbook("data.xls")
    sh = data.sheet_by_index(0)
    transaction = 0
    sales = 0
    dict = []
    for rx in range(1,sh.nrows):
        time = datetime.strptime(sh.row(rx)[0].value, "%Y-%m-%d %H:%M:%S").timestamp()
        
        #find the nearest time bucket
        if rx == 1:
            nearest = (time//(60*15))*(60*15)
            start = nearest
            timeslot = start + (60*15)
        
        #calculate the amount    
        if time <= timeslot:
            transaction = transaction + 1
            sales = sales + sh.row(rx)[1].value
            
        if time > timeslot:
            dict.append((datetime.fromtimestamp(start).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "{:.2f}".format(sales), transaction))
            sales = sh.row(rx)[1].value
            transaction = 1
            start = timeslot
            timeslot = start + (60*15)
         
    with open("case2_data.csv", 'w') as csvfile:
        csv_out=csv.writer(csvfile)
        csv_out.writerow(['Time', 'Sales', 'Transactions'])
        for data in dict:
            csv_out.writerow(data)


if __name__ == "__main__":
    main()