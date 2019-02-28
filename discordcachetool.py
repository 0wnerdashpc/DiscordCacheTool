import os, shutil, glob

try:
    user = input('Please enter your PC username, you can find this at C:\\Users\\NAMEHERE\n')
    source_dir = 'C:/Users/'+user+'/AppData/Roaming/Discord/Cache/'
    target_dir = 'C:/Users/'+user+'/Desktop/DiscordImgs/'
    shutil.copytree(source_dir, target_dir)
    for filename in glob.iglob(os.path.join(target_dir, '*.*')):
        os.rename(filename, filename+'.png')
    print('Complete, you can now find those files on your desktop.')
except:
    print('Error Encountered\nDelete the discordimg folder\nClose out of Discord\nRun the script again.')
    pass