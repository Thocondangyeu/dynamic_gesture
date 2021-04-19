import os
import glob
import argparse

args = argparse.ArgumentParser()
args.add_argument('--n', type=str,
                    help='name of new subject')
args.add_argument("--g" , type = str , help = "name of gesture" , default="all")



args = args.parse_args()

Gesture= args.g 
name_subject = args.n 

if Gesture == "all":
    folders = glob.glob("data/*/{}".format(name_subject))
    for folder in folders :
        #command = "rm -rf {}".format(folder)
        #os.system(command)
        os.remove(folder)
else :
    folders = glob.glob("data/{}/{}".format(Gesture,name_subject))
    for folder in folders :
        #command = "rm -rf {}".format(folder)
        #os.system(command)
        os.remove(folder)