import numpy as np
import os

class params():

    def __init__(self,experiment_name,parameters,filename='params.txt'):
        self.cwd        = os.getcwd()
        self.experiment = experiment_name
        self.parameters = parameters
        self.filename   = filename
        
        if os.path.isfile(self.cwd+'/'+self.filename):
            print('\nfile exists\n')
            mode = "a+"
            self.file       = open(self.filename,mode)
        else:
            print('\nfile '+self.filename+' is created\n')
            mode = "w+"
            self.file       = open(self.filename,mode)
            self.file.write("Experiment\t\t\t")
            for param in self.parameters.keys():
                print("parameter is: ",param)
                self.file.write(param)
                self.file.write("\t\t\t")
            self.file.write("\n")
        self.file.write(str(self.experiment))
        self.file.write("\t\t\t")
        for value in self.parameters.values():
            print("value is    :  ",value)
            self.file.write(str(value))
            self.file.write("\t\t\t")
        self.file.write("\n")        
        self.file.close()

class import_params():

    def __init__(self,filename,filepath=None):

        self.filename           = filename
        self.filepath           = filepath

        if self.filepath != None:
            self.filepath = filepath
            os.chdir(self.filepath)

        self.cwd                = os.getcwd()
        print('Current Directory is: ',self.cwd)
        self.parameters  = {}
        counter     = 0
        list_header = []
        list_params = []
        if os.path.isfile(self.cwd+'/'+self.filename):
            print('\nfile exists\n')
            mode = "r"
            self.file = open(self.filename,mode)
            for line in self.file:
                if counter == 0:
                    print('Headers are as follows:\n')
                    for word in line.split():
                        print(word)
                        list_header.append(word)
                    for ii in range(len(list_header)+1):
                        list_params.append(None)
                        list_params[ii] = []
                    print('\n')
                else:
                    col = 0
                    for word in line.split(sep="\t\t\t"):
                        list_params[col].append(word)
                        col = col + 1                            
                counter = counter + 1
            for ii in range(len(list_header)):
                self.parameters[str(list_header[ii])] = list_params[ii]
        else:
            print('File does not exist!')
        #print("The number of the experiment is %s\n" % (counter-1))
        #print("parameter headers are: ",self.parameters.keys())
        #print("\n")
        #print("parameters are       : ",self.parameters.values())
        

