
#Windows file directory
file_path_in_windows="C:\my-directory\target-file.txt"

#Windows file directory written in Python
le_path_for_windows_in_python="C:/my-directory/target-file.txt."

#CWD command: 
pwd_ =os.getcwd() 

#CWD command for external files:
pwd_external= outputs['current_directory_before'] = os.getcwd() 

# Liste of file
liste_of_files= outputs['fiels_and_directories'] = os.listdir() 

path_as_env=outputs['path_value'] = os.environ.get("PATH") 