import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    try:import DUMP 
    except:import DUMP
elif bit=='32bit':
    import DUMP32
