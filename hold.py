filtered_scenarios = scenarios[scenarios['body-area'].isin(['Chest-abdomen', 'Chest-abdomen-pelvis', 'Abdomen-pelvis', 'Abdomen', 'Pelvis'])]
body_area_n = len(filtered_scenarios)
print(f"Number of filtered scenarios by body area: {body_area_n}")

filtered_scenarios = filtered_scenarios[filtered_scenarios['panel'] != 'Pediatric']
without_peds_n = len(filtered_scenarios)
print(f"Number of filtered scenarios without pediatric: {without_peds_n}")

filtered_scenarios = filtered_scenarios[~filtered_scenarios['scenario-text'].str.contains('pregnant', case=False, na=False)]
without_pregnant_n = len(filtered_scenarios)
print(f"Number of filtered scenarios without pregnant: {without_pregnant_n}")

filtered_scenarios = filtered_scenarios[filtered_scenarios['panel'] != 'Interventional Radiology']
without_IR_n = len(filtered_df)
print(f"Number of filtered scenarios without IR: {without_IR_n}")
