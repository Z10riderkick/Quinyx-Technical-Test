import xlrd
from datetime import datetime
import csv

#15min constant
CONST_15min = 60*15

def main():
    #the newest version of xlrd no longer supporting xlsx file
    data = xlrd.open_workbook("data.xls")
    sh = data.sheet_by_index(0)
    transaction = 0
    sales = 0
    dict = []
    for rx in range(1,sh.nrows):
        time = datetime.strptime(sh.row(rx)[0].value, "%Y-%m-%d %H:%M:%S").timestamp()
        
        #find the nearest time bucket
        if rx == 1:
            nearest = (time//CONST_15min)*CONST_15min
            start = nearest
            timeslot = start + CONST_15min
        
        #calculate the amount    
        if time < timeslot:
            transaction = transaction + 1
            sales = sales + sh.row(rx)[1].value
        
        #save & reset    
        if time >= timeslot:
            dict.append((datetime.fromtimestamp(start).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "{:.2f}".format(sales), transaction))
            sales = sh.row(rx)[1].value
            transaction = 1
            start = (time//CONST_15min)*CONST_15min
            
            #fix the gap
            timeslot = timeslot + CONST_15min
            while (timeslot < start):
                dict.append((datetime.fromtimestamp(timeslot).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "{:.2f}".format(0), 0))
                timeslot = timeslot + CONST_15min
                
    dict.append((datetime.fromtimestamp(start).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "{:.2f}".format(sales), transaction))
    
    #save in csv file   
    with open("case2_data.csv", 'w', newline='') as csvfile:
        csv_out=csv.writer(csvfile)
        csv_out.writerow(['Time', 'Sales', 'Transactions'])
        for data in dict:
            csv_out.writerow(data)


if __name__ == "__main__":
    main()