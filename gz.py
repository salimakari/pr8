import gzip

NNat = 3981
NMet = 2600


with gzip.open('UP000509241.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).strip()
        if line.find("KW   Transmembrane {") != -1:
            i += 1
    print(f"Transembrane Natrinema share: {i/NNat:.4f}")



with gzip.open('UP000509594.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).strip()
        if line.find("KW   Transmembrane {") != -1:
            i += 1
    print(f"Transmembrane Methanolobus share: {i/NMet:.4f}")




with gzip.open('UP000509241.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).lower().strip()
        if line.find("de   recname:") != -1:
            if line.find("ase") != -1:
                i += 1
            if line.find("enzyme") != -1 and line.find("coenzyme") == -1:
                i += 1
    print(f"Enzyme Natrinema share: {i/NNat:.4f}")
          

with gzip.open('UP000509594.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).lower().strip()
        if line.find("de   recname:") != -1:
            if line.find("ase") != -1:
                i += 1
            if line.find("enzyme") != -1 and line.find("coenzyme") == -1:
                i += 1
    print(f"Enzyme Methanolobus share: {i/NMet:.4f}")
          

with gzip.open('UP000509241.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).lower().strip()
        if line.find("photo-lyase") != -1:
            i += 1
    print('Natrinema photo-lyase count:', i)

with gzip.open('UP000509594.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).lower().strip()
        if line.find("name") != -1:
            if line.find("photo-lyase") != -1:
                i += 1
            if line.find("photolyase") != -1:
                i += 1
    print('Methanolobus photo-lyase count:', i)


import gzip


with gzip.open('UP000509241.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).lower().strip()
        if line.startswith("b'de"):
            if line.find('recname') != -1:
                if line.find("rhodopsin") != -1:
                    i += 1
                elif line.find("photosystem") != -1:
                    i += 1
                elif line.find("photosyn") != -1:
                    i += 1
    print('Natrinema photosynthesis count:', i)



with gzip.open('UP000509594.swiss.gz','r') as fl: 
    i = 0       
    for line in fl:
        line = str(line).lower().strip()
        if line.startswith("b'de"):
            if line.find('recname') != -1:
                if line.find("rhodopsin") != -1:
                    print(line)
                elif line.find("photosystem") != -1:
                    print(line)
                elif line.find("photosyn") != -1:
                    print(line)
    print('Methanolobus photosynthesis count:', i)

    
is_reading =  False
with open ("output1.txt", "w") as out1:
    with gzip.open('UP000509241.swiss.gz','r') as fl:
        for line in fl:
            line = str(line).strip()
            new_line = "".join(filter(str.isupper, line))
            if is_reading:
                out1.write(new_line)
            if new_line.find("SQ") != -1:
                is_reading = True
            if new_line.find("//") != -1:
                is_reading = False


E = 0
D = 0
Num = 0
with open("output1.txt", "r") as seq1:
    for line in seq1:
        Num += len(line)
        E += line.count("E")
        D += line.count("D")

print(f"Natrinema Glu: {E/Num:.4f}%  Asp: {D/Num:.4f}% ")



is_reading =  False
with open ("output2.txt", "w") as out2:
    with gzip.open('UP000509594.swiss.gz','r') as fl:
        for line in fl:
            line = str(line).strip()
            new_line = "".join(filter(str.isupper, line))
            if is_reading:
                out2.write(new_line)
            if new_line.find("SQ") != -1:
                is_reading = True
            if new_line.find("//") != -1:
                is_reading = False





E = 0
D = 0
Num = 0
with open("output2.txt", "r") as seq2:
    for line in seq2:
        Num += len(line)
        E += line.count("E")
        D += line.count("D")

print(f"Methanolobus Glu: {E/Num:.4f}%  Asp: {D/Num:.4f}% ")

import os

if os.path.exists("output2.txt"):
    os.remove("output2.txt")


if os.path.exists("output1.txt"):
    os.remove("output1.txt")