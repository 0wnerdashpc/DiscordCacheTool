import os, shutil

try:
    user = os.environ.get('USERNAME')
    source_dir = 'C:/Users/'+user+'/AppData/Roaming/Discord/Cache/'
    target_dir = 'C:/Users/'+user+'/Desktop/DiscordImgs/'
    try:
        shutil.copytree(source_dir, target_dir)
    except:
        print('DiscordImgs folder found, removing and recreating the directory.')
        shutil.rmtree(target_dir)
        shutil.copytree(source_dir, target_dir)
        print('Done, continuing.')
    for filename in os.listdir(target_dir):
        os.rename(os.path.join(target_dir, filename), os.path.join(target_dir, filename+'.jpg'))
    print('Complete, you can now find those files on your desktop.')
except: #While this most likely a bad practice, the only errors encountered during testing were No.13 errors, which are access errors.
    print('Error Encountered\nClose out of Discord\nRun the script again.')