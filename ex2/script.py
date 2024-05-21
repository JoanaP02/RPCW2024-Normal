
# Criar sript que à ontologia acima adicione a partir de Disease_Syntoms.csv vais criar instâncias de doença (:Disease) para cada doença;

#open csv file

import csv

with open('Disease_Syntoms.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # criar dicionario com doença: sintomas
    diseases = {}
    for row in reader:
        symptoms = [row[f'Symptom_{i}'].strip() for i in range(1, 18) if row[f'Symptom_{i}']]
        if symptoms:
            diseases[row['Disease']] = symptoms
# adicionar Disease instances

ttl = f'''@prefix : <http://www.example.org/disease-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix swrl: <http://www.w3.org/2003/11/swrl#> .
@prefix swrlb: <http://www.w3.org/2003/11/swrlb#> .

:Ontology a owl:Ontology .

# Classes
:Disease a owl:Class .
:Symptom a owl:Class .
:Treatment a owl:Class .
:Patient a owl:Class .

# Properties
:hasSymptom a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Symptom .

:hasTreatment a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Treatment .

:exhibitsSymptom a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Symptom .

:hasDisease a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Disease .

:receivesTreatment a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Treatment .

# Disease instances
:Flu a :Disease ;
    :hasSymptom :Fever, :Cough, :SoreThroat ;
    :hasTreatment :Rest, :Hydration, :AntiviralDrugs .

:Diabetes a :Disease ;
    :hasSymptom :IncreasedThirst, :FrequentUrination, :Fatigue ;
    :hasTreatment :InsulinTherapy, :DietModification, :Exercise .

# Symptom instances
:Fever a :Symptom .
:Cough a :Symptom .
:SoreThroat a :Symptom .
:IncreasedThirst a :Symptom .
:FrequentUrination a :Symptom .
:Fatigue a :Symptom .

# Treatment instances
:Rest a :Treatment .
:Hydration a :Treatment .
:AntiviralDrugs a :Treatment .
:InsulinTherapy a :Treatment .
:DietModification a :Treatment .
:Exercise a :Treatment .


# Patient instances
:Patient1 a :Patient ;
    :name "Paul Harrods" ;
    :exhibitsSymptom :Fever ;
    :exhibitsSymptom :Cough ;
    :exhibitsSymptom :SoreThroat .

:Patient2 a :Patient ;
    :name "Ana Montana" ;
    :exhibitsSymptom :IncreasedThirst ;
    :exhibitsSymptom :FrequentUrination ;
    :exhibitsSymptom :Fatigue .
'''


# adicionar Disease instances and Symptom instances
for disease, symptoms in diseases.items():
    disease = disease.replace(' ', '_').replace('(', '_').replace(')', '_')
    modified_symptoms = []
    for symptom in symptoms:
        symptom = symptom.replace(' ', '_').replace('(', '_').replace(')', '_')
        modified_symptoms.append(symptom)

    ttl += f'\n:{disease} a :Disease ;\n'
    ttl += f'    :hasSymptom {", ".join([f":{symptom}" for symptom in modified_symptoms])} .\n'
    for symptom in modified_symptoms:
        ttl += f'\n:{symptom} a :Symptom .\n'

# ler Disease_Description.csv

with open('Disease_Description.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    descriptions = {row['Disease']:row['Description'].replace('"',' ') for row in reader}


for disease, description in descriptions.items():
    disease = disease.replace(' ', '_').replace('(', '_').replace(')', '_')
    ttl += f'\n:hasDescription a owl:DatatypeProperty ;\n'
    ttl += f'    rdfs:domain :Disease ;\n'
    ttl += f'    rdfs:range xsd:string .\n'
    ttl += f'\n:{disease} :hasDescription "{description}" .\n'


#A partir de Disease_Treatment.csv vais criar uma instância para cada tratamento
#se esta ainda não existir;

with open('Disease_Treatment.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Disease,Precaution_1,Precaution_2,Precaution_3,Precaution_4

    #dic with treatment : precautions
    treatments = {row['Disease'].replace(' ','_').replace('(', '_').replace(')', '_'): [row[f'Precaution_{i}'].replace(' ','_').replace('(', '_').replace(')', '_') for i in range(1, 5) if row[f'Precaution_{i}']] for row in reader}

#A partir de Disease_Treatment.csv vais criar uma instância para cada tratamento
#se esta ainda não existir;

for disease, precautions in treatments.items():
    disease = disease.replace(' ', '_').replace('(', '_').replace(')', '_')
    modified_precautions = []
    for precaution in precautions:
        precaution = precaution.replace(' ', '_').replace('(', '_').replace(')', '_')
        modified_precautions.append(precaution)
        if f':{precaution} a :Treatment' not in ttl:
            ttl += f'\n:{precaution} a :Treatment .\n'
    ttl += f'\n:{disease} :hasTreatment {", ".join([f":{precaution}" for precaution in modified_precautions])} .\n'
    
import json

#A partir de pgXXXXX.json que está na pasta doentes vais criar as instâncias dos
##doentes: um doente deverá ter um id (usa a tua imaginação), um nome (extraído do dataset) e uma
#lista de sintomas associados (extraídos do dataset);#

# [{"nome": "Vict\u00f3ria Michele Celinho", "sintomas": ["vomiting", "indigestion", "loss_of_appetite", "abdominal_pain", "passage_of_gases", "internal_itching"]}, {"nome": "Merita Bule", "sintomas": ["skin_rash", "joint_pain", "skin_peeling", "small_dents_in_nails", "inflammatory_nails"]},
with open('pg53895.json') as jsonfile:
    data = json.load(jsonfile)
    pacientes = {}
    i = 1  # Initialize counter
    for paciente in data[:100]:  # Iterate over the first 100 patients in the data
        original_name = paciente['nome']  # Store the original name
        pacientes[f'Patient{i}'] = {'nome': original_name, 'sintomas': paciente['sintomas']}  # Use the counter to create a unique ID
        i += 1  # Increment the counter

for paciente_id, paciente_data in pacientes.items():
    paciente_name = paciente_data['nome'].replace(' ', '_').replace('(', '_').replace(')', '_')
    modified_sintomas = []
    for sintoma in paciente_data['sintomas']:
        sintoma = sintoma.replace(' ', '_').replace('(', '_').replace(')', '_')
        modified_sintomas.append(sintoma)
    ttl += f'\n:{paciente_id} a :Patient ;\n'
    ttl += f'    :name "{paciente_name}" ;\n'
    ttl += f'    :exhibitsSymptom {", ".join([f":{sintoma}" for sintoma in modified_sintomas])} .\n'
    
with open('med_doentes.ttl', 'w') as ttlfile:
    ttlfile.write(ttl)      

