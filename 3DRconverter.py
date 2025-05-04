import sys 
import csv 

#3DR Converter for creating a readable cogo points csv file for 3DR converter 

def main(): 
    file_name = sys.argv[1] 

    point_number = [] 

    x = [] 
    y = [] 
    z = []

    raw_descript = [] 

    with open(file_name, 'r') as f: 
        reader = csv.reader(f, delimiter = ',')  

        data_len = 0 


        #reads all columns into each respective attribute type
        for row in reader: 

            if row[0] == '': 
                raw_descript.append("1000")  

            else: 
                point_number.append(row[0]) 

            if row[4] ==  '': 
                raw_descript.append("UKN") 

            else: 
                raw_descript.append(row[4]) 

            x.append(row[2]) 
            y.append(row[1]) 
            z.append(row[3]) 
            print(raw_descript) 
            data_len += 1 



    print(data_len)
    
    size = len(file_name) 

    output_file_name = file_name[:size - 4] 
            
    data_len = len(point_number) 



    #outputs each set of data into the appropriate columns
    with open(output_file_name + '.3DR.csv', 'w', encoding = 'UTF8', newline = '') as f: 
        writer = csv.writer(f, delimiter = ",", lineterminator = "\n") 

        for row in range(data_len): 
            f.write(raw_descript[row]) 
            f.write(",") 
            f.write(y[row]) 
            f.write(",") 
            f.write(x[row]) 
            f.write(",") 
            f.write(z[row]) 
            f.write(",") 
            f.write(point_number[row])
            f.write("\n") 
            


if __name__ == "__main__": 
    main()
    




