#! /usr/bin/python

import os, fnmatch
import sys
import time
from datetime import datetime
from threading import Timer

def intro():
        
        os.system("clear")
        
        print "\n**********************************************************************************************************************************************\n"
        print "\n"
        print "          #####################################################################"
        print "          ##                                                                 ##"
        print "          ##            ############                #############            ##"
        print "          ##            #############        ##     ############             ##"
        print "          ##                       ##        ##            ###               ##"
        print "          ##            #############   #### #####       ###                 ##"
        print "          ##            ############    ##### ####     ###                   ##"
        print "          ##            ###                ##        ############            ##"
        print "          ##            ###                ##       #############            ##"
        print "          ##                                                                 ##"
        print "          ##-----------------------------------------------------------------##"
        print "          ##                                                                 ##"
        print "          ##                Multiple_DSY_handler.py  (c) 2019                ##"
        print "          ##                          version 1.00                           ##"
        print "          ##                           R. Felecan                            ##"
        print "          ##                        ARRK Engineering                         ##"
        print "          ##                                                                 ##"
        print "          ##                        Mod.: 08.03.2019                         ##"
        print "          ##                                                                 ##"
        print "          ##-----------------------------------------------------------------##"
        print "          ##                                                                 ##"
        print "          ##                ###                                              ##"
        print "          ##               ####                                              ##"
        print "          ##              #####   #########    #########    ###   ###        ##"
        print "          ##             ######   ##########   ##########   ###  ###         ##"
        print "          ##            ### ###   ###     ##   ###     ##   #######          ##"
        print "          ##           ###  ###   ##########   ##########   ######           ##"
        print "          ##          ###   ###   #########    #########    ### ###          ##"
        print "          ##         ###    ###   ###    ###   ###    ###   ###  ###         ##"
        print "          ##        ###     ###   ###     ###  ###     ###  ###   ###        ##"
        print "          ##                                                                 ##"
        print "          #####################################################################"
        print "\n"
        print "\n**********************************************************************************************************************************************\n"

intro()

print "\nWelcome to the multiple .DSY-files handler script!"

while True:
        a4db_cue = raw_input("\nDo you want the script to save an .a4db-file? [y/n] ... ")
        if a4db_cue == "y" or a4db_cue == "n":
                break

exit_cue = "n"

if a4db_cue == "y":
        while True:
                exit_cue = raw_input("\nDo you want Animator to exit after saving the .a4db-file? [y/n] ... ")
                if exit_cue == "y" or exit_cue == "n":
                        break

while True:
        timer_cue = raw_input("\nDo you want to set a timer for starting the process later on? [y/n] ... ")
        if timer_cue == "y" or timer_cue == "n":
                break

functions_list_file = os.getcwd() + "/functions_list.txt"

fobj = open(functions_list_file, "w")
fobj.close()

while True:
        functions_selection = raw_input("\nDo you want to select any specific functions? [y/n] ... ")
        if functions_selection == "y" or functions_selection == "n":
                break

if functions_selection == "y":
        print "\nWhat type of entity do you need functions/vectors/tensors for (can be one or more)?"
        print "\n1. Functions - Shell elements"
        print "\n2. Functions - Membrane elements"
        print "\n3. Functions - Solid elements"
        print "\n4. Functions - Beam/Bar/Plink elements"
        print "\n5. Functions - Nodal"
        print "\n6. Functions - Pid"
        print "\n7. Vectors"
        print "\n8. Tensors"

        functions_for_elem_type = raw_input("\nWhat type of functions do you need? (ex. 1 3) ... ")

        functions_list = functions_for_elem_type.split(" ")
        functions_list_length = len(functions_list)

        for k in range(0, functions_list_length):
                if functions_list[k] == "1":
                        intro()
                        print "\nPlease select one or more functions for shell elements ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/shell_elements_functions.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
                
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/shell_elements_functions.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break
                        
                        
                        
                if functions_list[k] == "2":
                        intro()
                        print "\nPlease select one or more functions for membrane elements ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/membrane_elements_functions.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
                
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/membrane_elements_functions.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break
        
        
        
                if functions_list[k] == "3":
                        intro()
                        print "\nPlease select one or more functions for solid elements ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/solid_elements_function.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
        
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/solid_elements_function.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break


                if functions_list[k] == "4":
                        intro()
                        print "\nPlease select one or more functions for beam/bar elements ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/beam_bar_plink_elements.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
                
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/beam_bar_plink_elements.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break


                if functions_list[k] == "5":
                        intro()
                        print "\nPlease select one or more functions for nodes ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/nodal_function.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
                
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/nodal_function.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break
        
                if functions_list[k] == "6":
                        intro()
                        print "\nPlease select one or more functions for pids ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/pid_functions.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
                
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/pid_functions.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break

                if functions_list[k] == "7":
                        intro()
                        print "\nPlease select one or more vectors ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/vectors.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
                
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/vectors.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break

                if functions_list[k] == "8":
                        intro()
                        print "\nPlease select one or more tensors ... "
                        print ""
                        with open("/na/home/felecanhrisca/bin/tensors.txt") as f:
                                for i, line in enumerate(f):
                                        print ("        {0}. {1}".format(i+1,line[11:]))
                        elements = raw_input("\nWrite the index of the functions you need (ex. 1 6 13) ...")
                
                        elements_functions_list = elements.split(" ")
                
                        elements_functions_list_length = len(elements_functions_list)
                
                        fobj = open("/na/home/felecanhrisca/bin/tensors.txt", "r")
                        variants = [line.strip() for line in fobj]
                        fobj.close()
                
                        while True:
                                for i in range (0, elements_functions_list_length):
                                        for j, line in enumerate(variants):
                                                if elements_functions_list[i] == str(j+1):
                                                        fobj = open(functions_list_file, "a")
                                                        fobj.write(line + "\n")
                                                        fobj.close()
                                break

runs_directory = fnmatch.filter(os.listdir("."), "AU*")
runs = [line.strip() for line in runs_directory]

home = os.getcwd()

# Generating the a4 session-file

session = os.getcwd() + "/session.ses"
start_cue = os.getcwd() + "/start_cue"

fobj = open(session, "w")
fobj.write("$ This is the \"One time use\" session-file for animator\n")
fobj.close()

fobj = open(start_cue, "w")
fobj.write("$ This is the start cue of Animator. If the name of this document is \"done\", it means that Animator started :)")
fobj.close()

fobj = open(session, "a")
fobj.write("opt sys /bin/mv " + home + "/start_cue " + home + "/done\n")
fobj.close()

for line in runs:

        if os.path.exists(line + "/Output/"):
                os.chdir(line + "/Output/")                
        else:
                os.chdir(line)

        current_dir = os.getcwd()
        
        dateiliste = os.listdir(".")

        dateien = [line.strip() for line in dateiliste]

        dsygefunden = False

        for line in dateien:
                if ".DSY" in line:
                        if not "DSY.fzip.log" in line:
                                if not "D1.DSY.fzip" in line:
                                        dsyfile = line
                                        dsygefunden = True
                if ".THP" in line:
                        thpfile = line

        if  dsygefunden == True:
                fobj = open(session, "a")
                fobj.write("s[new]:rea geo Pamcrash " + current_dir + "/" + dsyfile + "\n")
                fobj.write("s[{VLASTSLOT}]:rea dis Pamcrash " + current_dir + "/" + dsyfile + " all\n")
                with open(functions_list_file) as g:
                        for line in g:
                                fobj.write("s[{VLASTSLOT}]:rea fil \"Pamcrash\" \"" + current_dir + "/" + dsyfile + "\" " + line[:-1] + "\"\n")
                fobj.close()
        last_run_dir = current_dir
        os.chdir(home)

variant = dsyfile[0:5]

fobj = open(session, "a")
#fobj.write("rea tcl " + "/na/home/felecanhrisca/bin/thp2list " + last_run_dir + "/" + thpfile + "\n")
#fobj.write("rea tcl " + "/na/home/felecanhrisca/bin/followerfinden " + last_run_dir + "/" + thpfile + "\n")
fobj.write("rea ses " + "/na/home/felecanhrisca/bin/" + variant + "_coloring_file.ses\n")
fobj.write("vie fo3 {VSoptfollowid1}/{VSoptfollowid2}/{VSoptfollowid3}\n")
fobj.write("opt sys /bin/rm " + home + "/functions_list.txt " + home + "/session.ses\n")
fobj.close()

if a4db_cue == "y":
        fobj = open(session, "a")
        fobj.write("wri da4 " + home + "/Animator_database.a4db\n")
        if exit_cue == "y":
                fobj.write("bye")
        fobj.close()

tool_animator = "echo 62 | a3"

# session --> session-file (including complete path to it)

if exit_cue == "y":
        a4_start = tool_animator + " -FG -w 1200 -h 800 -b -s " + session + " 2>/dev/null"
else:
        a4_start = tool_animator + " -FG -w 1200 -h 800 -s " + session + " 2>/dev/null"

# Animator recursive startup with licence check

def Animator_start():
        os.system(a4_start)
        while True:
                exists = os.path.isfile(home + "/done")
                if exists == True:
                        break
                        sys.exit(0)
                else:
                        print "No licenses available. We'll try again in 5 seconds..."
                        time.sleep(5)
                        os.system(a4_start)
                        sys.exit(0)


if timer_cue == "y":

        intro()

        x = datetime.today()
        
        print "\nCurrent date and time is ... " + str(x)
        
        print"\nPlease write here when you want the process to start ... "
        
        time.sleep(1)
        
        start_month = raw_input("\nMonth ... ")

        start_day = raw_input("\nDay ... ")
        
        start_hour = raw_input("\nHour ... ")
        
        start_minute = raw_input("\nMinute ... ")
        
        delta_day = int(start_day) - int(x.day)
        
        delta_month = int(start_month) - int(x.month)
        
        y=x.replace(month = x.month + delta_month, day = x.day + delta_day, hour = int(start_hour), minute = int(start_minute), second=0, microsecond=0)
        
        intro()
        
        print "\nThe process will start on ... " + str(y)
        
        print ""
        
        delta_t=y-x
        
        secs=delta_t.seconds+1
        
        if __name__ == "__main__":
                try:
                        pid = os.fork()
                        if pid > 0:
                                sys.exit(0)
                except OSError, e:
                        print >> sys.stderr, "fork failed: %d (%s)" % (e.errno, e.strerror)
                        sys.exit(1)

                os.chdir("/")
                os.setsid()
                os.umask(0)
        
        def startup():
                Animator_start()
        t = Timer(secs, startup)
        t.start()
else:
        intro()
        
        print "\nAnimator will start now ..."
        
        if __name__ == "__main__":
                try:
                        pid = os.fork()
                        if pid > 0:
                                sys.exit(0)
                except OSError, e:
                        print >> sys.stderr, "fork failed: %d (%s)" % (e.errno, e.strerror)
                        sys.exit(1)

                os.chdir("/")
                os.setsid()
                os.umask(0)
        
        Animator_start()
