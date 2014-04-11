import os, subprocess, glob
#set path to folder containing xls files 
path='C:\Users\RossBehavioralLab\Desktop\SeanMa\New_CulturalSEAT\Conditions'
os.chdir(path)
#find all files with extension .xls
xlsx=glob.glob('*.xlsx')
#create output filenames with extensions .csv
csvs = [x.replace('.xlsx','.csv') for x in xlsx]
#zip into a list of tuples
in_out=zip(xlsx,csvs)
#loop through each file, calling the in2csv ultility from subprocesses
for xl,csv in in_out:
    out=open(csv,'w')
    command='C:\Users\RossBehavioralLab\Downloads\csvkit\csvkit\utilities\in2csv %s\\%s' %(path,xl)
    proc=subprocess.Popen(command,stdout=out)
    proc.wait()
    out.close()

#Github test
