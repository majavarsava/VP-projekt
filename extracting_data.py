import zipfile
import os
import pandas as pd

# Postavi putanje do ZIP datoteka
national_zip = "names.zip"
state_zip = "namesbystate.zip"

# Stvori direktorije za ekstrakciju
os.makedirs("national_names", exist_ok=True)
os.makedirs("state_names", exist_ok=True)

# Ekstraktaj datoteke
with zipfile.ZipFile(national_zip, 'r') as zip_ref:
    zip_ref.extractall("national_names")

with zipfile.ZipFile(state_zip, 'r') as zip_ref:
    zip_ref.extractall("state_names")

# ----------------------------
# Nacionalni podaci (names.zip)
# ----------------------------

national_data = []

for filename in sorted(os.listdir("national_names")):
    if filename.startswith("yob") and filename.endswith(".txt"):
        year = int(filename[3:7])
        df = pd.read_csv(f"national_names/{filename}", names=["Name", "Gender", "Count"])
        df["Year"] = year
        national_data.append(df)

national_df = pd.concat(national_data, ignore_index=True)

# Spremi u CSV
national_df.to_csv("national_names.csv", index=False)
print("✅ Spremljeno: national_names.csv")

# ----------------------------
# Podaci po državama (namesbystate.zip)
# ----------------------------

state_data = []

for filename in sorted(os.listdir("state_names")):
    if filename.endswith(".TXT"):
        df = pd.read_csv(f"state_names/{filename}", names=["State", "Gender", "Name", "Year", "Count"])
        state_data.append(df)

state_df = pd.concat(state_data, ignore_index=True)

# Spremi u CSV
state_df.to_csv("state_names.csv", index=False)
print("✅ Spremljeno: state_names.csv")
