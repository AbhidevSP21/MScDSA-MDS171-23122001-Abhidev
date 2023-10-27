import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# Declared the function to calculate properties
def calculate_properties(smiles):
    mol = Chem.MolFromSmiles(smiles)
    properties = {}

    properties["Molecular Weight"] = Descriptors.MolWt(mol)
    properties["Number of Heavy Atoms"] = Descriptors.HeavyAtomMolWt(mol)
    properties["Fraction of Sp3 Carbon Atoms"] = Descriptors.FractionCSP3(mol)
    properties["Number of Rotatable Bonds"] = Descriptors.NumRotatableBonds(mol)
    properties["Number of Hydrogen Acceptors"] = Descriptors.NumHAcceptors(mol)
    properties["Number of Hydrogen Donors"] = Descriptors.NumHDonors(mol)
    properties["Molar Refractivity"] = Descriptors.MolMR(mol)
    properties["Polar Surface Area"] = Descriptors.TPSA(mol)
    properties["LogP (Partition Coefficient)"] = Descriptors.MolLogP(mol)

    print("Properties:")
    for prop, value in properties.items():
        print(f"{prop}: {value}")
    return properties

# Check if a compound follows Lipinski's Rule of Five
def check_lipinski(properties):
    mw = properties["Molecular Weight"]
    logp = properties["LogP (Partition Coefficient)"]
    h_acceptors = properties["Number of Hydrogen Acceptors"]
    h_donors = properties["Number of Hydrogen Donors"]
    
    if mw <= 500 and logp <= 5 and h_acceptors <= 10 and h_donors <= 5:
        print("Lipinski Rule of Five: Passed")
    else:
        print("Lipinski Rule of Five: Failed")

#  Ghose's Rule
def check_ghose(properties):
    logp = properties["LogP (Partition Coefficient)"]
    molar_refractivity = properties["Molar Refractivity"]
    mw = properties["Molecular Weight"]
    tpsa = properties["Polar Surface Area"]
    
    if -0.4 <= logp <= 5.6 and 40 <= molar_refractivity <= 130 and 160 <= mw <= 480 and 70 <= tpsa <= 120:
        print("Ghose's Rule: Passed")
    else:
        print("Ghose's Rule: Failed")

#Veber's Rule
def check_veber(properties):
    rotatable_bonds = properties["Number of Rotatable Bonds"]
    tpsa = properties["Polar Surface Area"]
    
    if rotatable_bonds <= 10 and tpsa <= 140:
        print("Veber's Rule: Passed")
    else:
        print("Veber's Rule: Failed")

#Egan's Rule
def check_egan(properties):
    logp = properties["LogP (Partition Coefficient)"]
    tpsa = properties["Polar Surface Area"]
    
    if logp <= 5.88 and tpsa <= 131.6:
        print("Egan's Rule: Passed")
    else:
        print("Egan's Rule: Failed")

#Muegge's Rule
def check_muegge(properties):
    mw = properties["Molecular Weight"]
    logp = properties["LogP (Partition Coefficient)"]
    tpsa = properties["Polar Surface Area"]
    num_heavy_atoms = properties["Number of Heavy Atoms"]
    rotatable_bonds = properties["Number of Rotatable Bonds"]
    h_acceptors = properties["Number of Hydrogen Acceptors"]
    h_donors = properties["Number of Hydrogen Donors"]
    
    if 200 <= mw <= 600 and -2 <= logp <= 5 and 150 <= tpsa <= 350:
        print("Muegge's Rule: Passed")
    else:
        print("Muegge's Rule: Failed")

# Check if a compound meets leadlikeness criteria
def check_leadlikeness(properties):
    mw = properties["Molecular Weight"]
    logp = properties["LogP (Partition Coefficient)"]
    rotatable_bonds = properties["Number of Rotatable Bonds"]
    
    if 250 <= mw <= 350 and logp <= 3.5 and rotatable_bonds <= 7:
        print("Leadlikeness: Passed")
    else:
        print("Leadlikeness: Failed")

# Get user input for the number of compounds
num_inputs = int(input("Enter the number of compounds: "))
smiles_list = []

# Collect SMILES(Simplified Molecular Input Line Entry System) notation for each compound
for i in range(num_inputs):
    smiles = input(f"Enter SMILES for Compound {i + 1}: ")
    smiles_list.append(smiles)

# Process each compound and check various rules
for i, smiles in enumerate(smiles_list):
    print(f"\nProperties for Compound {i + 1}:")
    calculate_properties(smiles)
    properties = calculate_properties(smiles)
    check_lipinski(properties)
    check_ghose(properties)
    check_veber(properties)
    check_egan(properties)
    check_muegge(properties)
    check_leadlikeness(properties)

# Create a DataFrame and save it to a CSV file
data = {
    "Molecular Weight": [],
    "Number of Heavy Atoms": [],
    "LogP (Partition Coefficient)": [],
    "Polar Surface Area": [],
    "Molar Refractivity": [],
    "Number of Hydrogen Donors": [],
    "Number of Hydrogen Acceptors": [],
    "Number of Rotatable Bonds": [],
    "Fraction of Sp3 Carbon Atoms": [],
}

for smiles in smiles_list:
    properties = calculate_properties(smiles)
    for prop in data.keys():
        data[prop].append(properties[prop])

df = pd.DataFrame(data)
df.to_csv("compound_properties.csv", index=False)


