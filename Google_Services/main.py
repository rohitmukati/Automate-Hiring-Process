from find_all_files_ids_in_folders import both_folder_files_id
from move_file import move_files_by_dict
from dotenv import load_dotenv
import os
 
load_dotenv()
PROCESSED_FOLDER_ID = os.getenv("PROCESSED_FOLDER_ID")
UNPROCESSED_FOLDER_ID = os.getenv("UNPROCESSED_FOLDER_ID")




processed_file_ids, unprocessed_file_ids = both_folder_files_id()
move_files_by_dict(unprocessed_file_ids, PROCESSED_FOLDER_ID)
