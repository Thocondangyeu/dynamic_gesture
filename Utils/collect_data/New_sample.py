import os 

import argparse 
import glob

args = argparse.ArgumentParser()
args.add_argument('--n', type=str,
                    help='name of new subject')
args = args.parse_args()


def command_gen(name) :
    command_file = open("command.txt","w")
    print("Generating command")
    
    for names in glob.glob("data/*"):
        for i in  range(1,4):
            ges = names.split("\\")[-1]
            command = "python multi_cam.py --g {} --n {} --i {} \n ".format(ges , name , i)
            
            command_file.write(command)

print(args.n)

folder_path = "data/*"
gestures = glob.glob(folder_path)
for gesture in gestures:
    command_gen(name = args.n )
    os.mkdir(gesture + "/"+args.n)