import os
import shutil
import datetime

def backup_server_data():
    source = 'discord-moderation-bot/data'
    backup_dir = 'discord-moderation-bot/data/backups'
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_name = 'backup_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup_dir, backup_name)
    
    try:
        shutil.copytree(source, backup_path)
        print("Server data backed up successfully to:", backup_path)
    except shutil.Error as e:
        print("Error: Failed to backup server data.")
        print(e)
    
backup_server_data()