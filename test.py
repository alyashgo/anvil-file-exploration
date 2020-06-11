import pandas as pd 
import xml.etree.ElementTree as etree
import os

tree = etree.parse("AALIM.anvil")
root = tree.getroot()

info=[]
column=['Preliminary Information.Name', 'Preliminary Information.Gender', 'Preliminary Information.Diagnosis', 'Play', 'Stereotypies.Motor', 'Stereotypies.Vocal/Verbal', 'Stereotypies.Visual', 'Sensory Issues.Auditory', 'Sensory Issues.Visual', 'Sensory Issues.Texture', 'Facial Expression/Emotional Response', 'Social Behaviour.Eye Contact', 'Social Behaviour.Social Interaction', 'Social Behaviour.Social Greetings', 'Joint Attention.Follows Gaze', 'Joint Attention.Follows a Point', 'Joint Attention.Shows objects spontaneously/Points to Show', 'Joint Attention.Shares happiness/ excitement', 'Expressive communication.Shakes head for No', 'Expressive communication.Nods for Yes', 'Expressive communication.Asks for Help', 'Expressive communication.Points to ask or choose', 'Expressive communication.Speech', 'Receptive communication.Response to Name', 'Receptive communication.Response to Smile', 'Imitation.Motor Imitation', 'Imitation.Actions on Objects', 'Imitation.Orofacial Imitation', 'Maladaptive Behaviour']
all =[]

"""
for filename in os.listdir(path):
    if not filename.endswith('.anvil'): continue
    fullname = os.path.join(path, filename)
    tree = etree.parse(fullname)
    root = tree.getroot() 
"""

for elem in tree.iter():
    
    if elem.attrib.get("name") in column:
        
        if elem.attrib.get("name") == column[0]:    #Preliminary Information.Name
            print(elem[0][0].text)

        if elem.attrib.get("name") == column[1]:    #Preliminary Information.Gender
            print(elem[0][0].text)

        if elem.attrib.get("name") == column[2]:    #Preliminary Information.Diagnosis
            print(elem[0][0].text)
        
        if elem.attrib.get("name") == column[3]:    #Play
            for child in elem:
                print(child[0].text)

        
    
    else:
        continue

#df = pd.DataFrame(all, columns=column)
#print(df)