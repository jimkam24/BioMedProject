import pandas as pd

meta = pd.read_csv("data/raw/iHMP_IBDMDB_2019/metadata.tsv", sep="\t")
genera = pd.read_csv("data/raw/iHMP_IBDMDB_2019/genera.tsv", sep="\t", index_col=0)

print("Metadata shape:", meta.shape)
print("Genera shape:", genera.shape)

print("\nDiagnosis counts:\n", meta["Study.Group"].value_counts())
print("\nGender counts:\n", meta["Gender"].value_counts())
print("\nAntibiotics counts:\n", meta["Antibiotics"].value_counts())
print("\nMissing values per column:\n", meta.isnull().sum())