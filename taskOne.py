#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import process utility library
import psutil
import platform

#menu items 
menu= { 1 : 'Percentage use of each CPU core in 10sec.', 2 : 'Ram usage in GB', 3 : 'operating System Name and Version' , 4 : 'Check is computer is Busy', 0 : 'Exit' }

#initialize variariable to enable script access the infinite loop
menuKey=1;

while menuKey > 0:
    print(f'{"":15s} Menu\n')
    for key, description in menu.items():
        print(f'{key:2d} : {description:32s}')
    
    menuKey=int(input("\nEnter a menu option or 0 to Exit : "))
    
    #get the percentage of each cpu core over 10secs 
    if menuKey==1:
        #prompt a message to indicate the program will be idle for few secounds
        print('\nWait, while program monitor cpu usage...')
        #get the percentage usage of all cpu cores
        cpu_per= psutil.cpu_percent(10, all)
        #display the percentage usage for each core
        for i in range(len(cpu_per)):
            print(f' {"core"+str(i):6s} : {str(cpu_per[i])+"%":6s}')
        print('\n')
    
    #get the RAM usage in GB
    elif menuKey==2:
        #get memory usage
        memory_details = psutil.virtual_memory()
        #convert to GigaByte by dividing by two in thirty times
        gb_usage = memory_details.used
        for i in range(30):
            gb_usage = gb_usage /2
        print(f'\n{gb_usage:.2f}GB has been used\n')
        
    #getting the operating system name and version
    elif menuKey==3:
        #display the system operating system and version
        #source : https://docs.python.org/3.11/library/platform.html?highlight=platform#module-platform
        print('System running on '+platform.system()+' version: '+platform.version()) 
        
        
    #check whether the computer is currently busy
    elif menuKey==4:
        #get percentage cpu usage 
        cpu_per= psutil.cpu_percent(1)
        #get percentage RAM usage
        memory_details = psutil.virtual_memory()        
        used_per= memory_details.percent
        
        if cpu_per >= 50 and used_per >= 50 :
            print('\nThe computer is busy\n')
        else:
            print('\nThe computer is not busy\n')
            
    #display  message to indicate an end to the program
    else:
        print('\nprogram terminated')


# In[ ]:




