import os

def create_folder_files():
    folder_name_1= "Mind_at_Ease"
    folder_name_2="Calender_Notes"
    folder_name_3="Calender_Statistics"
    
    
    #Εντοπισμοσ του Directory που βρισκεται το script
    script_directory=os.path.dirname("__file__")

    #Δημιουργια του ολοκληρωμενου path για το directory
    folder1_path=os.path.join(script_directory, folder_name_1)

    #Δημιουγια του γενικού φακέλου
    os.makedirs(folder_name_1, exist_ok=True)

    #Δημιουργια του ολοκληρωμενου path για το directory και του φακελου των καταγραφων
    folder1_folder2_path=os.path.join(folder_name_1, folder_name_2)
    #Δημιουργια του ολοκληρωμενου path για το directory και του φακελου των στατιστικων
    folder1_folder3_path=os.path.join(folder_name_1, folder_name_3)

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
    statistics_file_path=os.path.join(folder_name_4,"statistics notes.txt")

    #Ανοιγω το φακελο των Στατιστικων για να γραψω το περιεχομενο που ειναι ωσ ορισμα τησ συναρτησης
    with open(statistics_file_path, "w") as statistics_files:
        statistics_files.write(statistics_content)
 
    #Δημιουργια path που μας οδηγει στο φακελο των Καταγραφων
    cal_notes_file_path=os.path.join(folder_name_4,"calender notes.txt")

    #Ανοιγω το φακελο των Καταγραφων για να γραψω το περιεχομενο που ειναι ωσ ορισμα τησ συναρτησης
    with open(cal_notes_file_path, "w") as calender_notes_files_files:
        calender_notes_files_files.write(calendar_notes_content)


    print(f"Content saved to 'statistics.txt' and 'calendar_notes.txt'.")
   



if __name__=="__main__":
    create_folder_files()
