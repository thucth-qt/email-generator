
import json
import csv
import datetime

def read_json(path:str)->str:
    try:
        #linuxs
        f=open(path, mode='r', encoding='utf-8')
    except:
        #windows
        f=open(path, mode='r', encoding='cp1252')

    data_str = str(json.load(f))
    f.close()

    return data_str

def check_valid(data_dict:dict, not_null_list:list):
    for key in not_null_list:
        if (key not in data_dict) or (data_dict[key] is None):
            return False
    return True

def generate_email(template_path:str, custormer_info_path:str, output_path:str, error_path:str, not_null: list=['EMAIL'], id_field:str='FIRST_NAME') -> dict:
    '''
    Returns dictionary {<id> : <detail_email>}. 

            Parameters:
                    template_path (str): Path to the FILE contains email template.
                    custormer_info_path (str): Path to the FILE contains customer informations.
                    output_path (str): Path to the DIRECTORY of output.
                    error_path (str): Path to the FILE contains error outputs.
                    not_null (str): List of fields must be not empty.
                    id_field (str): Identification for each email.

            Returns:
                    output_returned (dict): Returns dictionary {<id> : <detail_email>}. Detail emails are templates filled with customers informations.
    '''
    template_str = read_json(template_path)
    output =str()
    output_returned =dict()

    with open(custormer_info_path, mode='r') as f:
        with open(error_path, mode='w+') as h:
            
            customer_reader = csv.DictReader(f, delimiter=',')
            error_writer = csv.DictWriter(h, fieldnames=customer_reader.fieldnames)
            error_writer.writeheader()

            for row in customer_reader:
                template_ = template_str
                
                # check missing information
                if(not check_valid(row,not_null)):
                    error_writer.writerow(row)
                    continue
                
                # fill into template
                for key in row.keys():
                    old_str = '{{'+key+'}}'
                    new_str = row[key]
                    template_ = template_.replace(old_str, new_str)
                today = datetime.date.today()
                template_ = template_.replace('{{TODAY}}', today.strftime("%d %b %Y"))

                # write results
                output_path_ = output_path.replace('{}', row[id_field])
                with open(output_path_, mode='w+') as g:
                    data_dict = json.loads(template_.replace("'","\""))
                    json.dump(data_dict,fp=g, indent=4)
                    output_returned[row[id_field]] = template_
         
    return output_returned