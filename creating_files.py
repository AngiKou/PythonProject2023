import os
import json
from pathlib import Path
from datetime import datetime

def create_folder_files():
    folder_name_0="Files"
    folder_name_1="Mind_at_Ease"
    folder_name_2="Calender_Notes"
    folder_name_3="Calender_Statistics"
    
    
    #Εντοπισμοσ του Directory που βρισκεται το script
    script_directory=os.path.dirname("__file__")

    #Δημιουργια του ολοκληρωμενου path για το directory
    folder0_path=os.path.join(script_directory, folder_name_0)

    #Δημιουγια του γενικού φακέλου
    os.makedirs(folder_name_0, exist_ok=True)

    #Δημιουργια του ολοκληρωμενου path για το directory και του φακελου των καταγραφων
    folder0_folder1_path=os.path.join(folder_name_0, folder_name_1)

    #Δημιουργια του ολοκληρωμενου path για το directory και του φακελου των καταγραφων
    folder1_folder2_path=os.path.join(folder0_folder1_path, folder_name_2)
    #Δημιουργια του ολοκληρωμενου path για το directory και του φακελου των στατιστικων
    folder1_folder3_path=os.path.join(folder0_folder1_path, folder_name_3)

    #Δημιουγια του υποφακέλου Καταγραφων με χρηση του αντιστιχου path If the folder already exists, do nothing (exist_ok=True)
    os.makedirs(folder0_folder1_path, exist_ok=True)    
    #Δημιουγια του υποφακέλου Καταγραφων με χρηση του αντιστιχου path If the folder already exists, do nothing (exist_ok=True)
    os.makedirs(folder1_folder2_path, exist_ok=True)
    #Δημιουγια του υποφακέλου Στατιστικων με χρηση του αντιστιχου path If the folder already exists, do nothing (exist_ok=True)
    os.makedirs(folder1_folder3_path, exist_ok=True)

    
    #Δημιουργια αρχειου καταγραφων ημερολογιου If the folder already exists, do nothing (exist_ok=True)
    calender_notes_file_path=os.path.join(folder1_folder2_path, "calender notes.txt") 
    #Ανοιγω το φακελο των Στατιστικων για να γραψω το τιτλο του αρχειου
    with open(calender_notes_file_path, "w") as calender_notes_file:
        calender_notes_file.write("These are the saved calender notes\n") 

    
    #Δημιουργια αρχειου στατιστηκων ημερολογιου
    calender_statistics_file_path= os.path.join(folder1_folder3_path,"statistics notes.txt")
    #Ανοιγω το φακελο των Στατιστικων για να γραψω το τιτλο του αρχειου
    with open(calender_statistics_file_path, "w") as calender_statistics_file:
        calender_statistics_file.write("These are the calender \n")


#Συναρτηση αποθηκευσης των δεδομενων του calender
def save_content_to_files (statistics_content,calendar_notes_content):
    folder_name_4="Calender_Statistics"
    folder_name_5="Calender_Notes"

    #Δημιουργια path που μας οδηγει στο φακελο των Στατιστικων στοιχειων 
    #statistics_file_path=os.path.join(folder_name_4,"statistics notes.txt")

    #Ανοιγω το φακελο των Στατιστικων για να γραψω το περιεχομενο που ειναι ωσ ορισμα τησ συναρτησης
   # with open(statistics_file_path, "w") as statistics_files:
       # statistics_files.write(statistics_content)
 
    #Δημιουργια path που μας οδηγει στο φακελο των Καταγραφων
    cal_notes_file_path=os.path.join(folder_name_5,"calender notes.txt")

    #Ανοιγω το φακελο των Καταγραφων για να γραψω το περιεχομενο που ειναι ωσ ορισμα τησ συναρτησης
    with open(cal_notes_file_path, "w") as calender_notes_files_files:
        calender_notes_files_files.write(calendar_notes_content)


    #print(f"Content saved to 'statistics.txt' and 'calendar_notes.txt'.")
   
def save_file():  #date_picked
    #file_name=date_picked
    #emotion_list=list_data
    #emotion_text=text
    folder_name_6="Calender_Statistics"
    folder_name_7="Calender_Notes"
    
   # file_name="_".join(date_picked.split("/"))

    #δημιουργια didtionary
    #Data_dic={emotion_list:[], "emotion_text":emotion_text}
    Data_dic={"anna":123456, "maria":23456}

    folder=Path(__file__).parent
    root_foler = Path(folder).parent
    #file_data=Path(root_foler, "Files",folder_name_7,f"{file_name}.txt")
    file_data=Path(root_foler, "Files","Mind_at_Ease",folder_name_7,"test.txt")
    #print(file_data)
    with open(file_data, "w") as f:
        json.dump(Data_dic,f)



# Function to convert file name to date
def convert_to_date(file_name):
    # Customize this function based on the file name format in your folder
    # This is just an example assuming the file name is in the format "YYYY-MM-DD.txt"
    date_string = file_name.split('_')[0]
    return datetime.strptime(date_string, '%Y-%m-%d')

# Function to count files where one is after the other based on date
def count_files_with_later_dates():
    folder_name_8="Calender_Notes"

    folder_path=Path(__file__).parent
    root_foler = Path(folder_path).parent
    file_data=Path(root_foler, "Mind_at_Ease",folder_name_8)

    # Get a list of file names in the specified folder
    files = sorted(os.listdir(file_data))

    # Initialize the count of files where one is after the other
    count = 0

    # Iterate through the files
    for i in range(len(files) - 1):
        # Convert the current file name to date
        current_date = convert_to_date(files[i])
        
        # Convert the next file name to date
        next_date = convert_to_date(files[i + 1])

        # Check if the current file's date is before the next file's date
        if current_date < next_date:
            # Increment the count if the condition is met
            count += 1

    # Return the final count
    return count



    

   





if __name__=="__main__":
    create_folder_files()
    save_file()







 
