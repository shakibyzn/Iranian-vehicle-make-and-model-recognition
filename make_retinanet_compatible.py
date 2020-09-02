# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:26:54 2020

@author: ASUS
"""

from bs4 import BeautifulSoup
import os
import csv

folder = 'retinanet_compatible/test/'
folder_name = ['images','labels']

cat = {'peugeot_405_slx':1, 'rio':2, 'peugeot_206':3, 'peugeot_504':4,
                         'pride_131':5, 'daewoo_cielo':6, 'megan':7, 'zamyad_truck':8, 
                         'mvm_530':9, 'lifan_620':10, 'pride_141':11, 'others':12, 'peykan_80':13,
                         'mvm_110':14, 'runna':15, 'kia_optima_2010':16, 'renault_l90':17, 'xantia':18,
                         'samand_soren':19, 'samand':20, 'mvm_315':21, 'peugeot_207':22, 'pride_132':23,
                         'mazda_truck':24, 'peugeot_pars':25, 'samand_soren_elx':26, 'peugeot_405':27
                         , 'tiba':28}

cat = dict((y,x) for x,y in cat.items())

with open('bbox-imgs-test.csv', mode='w', newline='') as file:
    
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
    
    file_labels = os.listdir(folder + folder_name[1])
    for file in file_labels:
        with open(folder + '/labels/' + file) as label_file:
            class_id = int(label_file.readlines()[0].split()[0]) 
            class_name = cat[class_id]
            handler = open(os.path.join('../newdataset/car_annotations/', file.split('.')[0] + '.xml')).read()
            soup = BeautifulSoup(handler, "xml")
            xmin = int(soup.xmin.string)
            xmax = int(soup.xmax.string)
            ymin = int(soup.ymin.string)
            ymax = int(soup.ymax.string)
            row = [file.split('.')[0] + '.jpg', xmin, ymin, xmax, ymax, class_name]
             
            writer.writerow(row)
            



