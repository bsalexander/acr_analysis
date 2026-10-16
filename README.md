# Descriptive analysis of the ACR appropriateness criteria for abdominal/pelvic emergency department presentations

Efforts to improve CT use have focused on evidence-based decision rules and clinical practice guidelines. Among these, the American College of Radiology (ACR) Appropriateness Criteria (AC) characterize imaging modalities as usually appropriate, may be appropriate, or usually not appropriate. We determined the frequency of CT and alternative imaging ratings in ACR AC for adult patients with abdominal complaints.

This analysis is based on [published ACR scenarios](https://gravitas.acr.org/acportal) [downloaded in Oct/Nov 2024](/supplemental/download_history.txt). 

Authors:
- Joshua Broder, MD (Corresponding author)
- Benjamin Alexander, MD
- Jennifer Evans, MD
- Kendrick Kennedy, MD

All authors are affiliated with Duke University Health.

## License

The analysis code and Jupyter notebook code in this repository are licensed under the MIT License. See [LICENSE](LICENSE).

Original supporting datasets, supplemental tables, and documentation are licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license, unless otherwise noted.

These licenses apply only to materials for which the authors hold the necessary rights. Third-party materials and restricted datasets are excluded.

Please cite the associated publication and archived repository DOI when using these materials.

## Steps for reproduction

This analysis was conducted on GitHub Codespaces. GitHub Copilot was used for coding assistance in developing Python/Jupyter notebooks for statistical analysis. All code and results were reviewed by the authors who retain full responsibility for their accuracy and integrity.

The results of the final analysis notebook are visible in this repository. Steps for recreation are listed below for those interested in exploring or modifying the code, but are not necessary to review code and results.

### Environment

Installed packages are documented in [requirements.txt](requirements.txt). Final analysis was conducted in [Python 3.12.1](.python-version).

If desired, you may create a virtual environment, then install exact dependencies with:
```
python -m pip install -r requirements.txt

python -m ipykernel install --user \
  --name research-analysis \
  --display-name "Python (research-analysis)"
```

### Execution

> [!IMPORTANT]
> It is not recommended to repeat steps 1-3 below. The ACR website is frequently updated and will not reflect data downloaded for this analysis.

> [!NOTE]
> During the original download, data was accessed in accordance with the [ACR website terms and conditions](ACR%20AC%20Terms%20and%20Conditions-20250103.txt") and the [ACR website robots.txt file](acr-2025-0103-robots.txt). 

1. The file [acr_ac_scenarios.csv](acr_ac_scenarios.csv) contains a list of clinical scenarios defined by the ACR and listed on their [Appropriateness Criteria portal](https://gravitas.acr.org/acportal). This list was copied from the portal in October 24. Each scenario contains a link to a page containing associated studies and their appropriateness ratings.
2. Script [01 scrape.py](01%20scrape.py) pulls study and appropriateness rating for each scenario. To reduce load on ACR web servers, this script was run on a single "panel" at a time on different days, and with a 10 second pause between each request. Download history is contained in [/supplemental/download_history.txt](/supplemental/download_history.txt)
3. Script [02 combine.py](02%20combine.py) combines separate panels into a common file for analysis.

#### Begin here

4. The Jupyter notebook [03 analyze.ipynb](03%20analyze.ipynb) contains the descriptive analysis. The notebook details the methods of restricting scenarios to abdominal complaints seen in the emergency department.
  - [include.csv](include.csv) contains scenarios that were originally **exluded** based on criteria filtering, but then later added back based on expert review.
  - [exclude.csv](exclude.csv) contains scenarios that were originally **included** based on criteria filtering, but then later removed based on expert review.
5. The directory /output contains the following files:
  - [category_grid.png](/output/category_grid.png) - 3x3 grid of study counts by appropriateness ranking.
  - [category_grid_initial.png](/output/category_grid_initial.png) - 3x3 grid of study counts by appropriateness ranking, when limited to studies designated as "initial imaging".
  - [modality_percentages.png](/output/modality_percentages.png) - frequency graph of modalities alternative to CT.
  - [modality_percentages_initial.png](/output/modality_percentages_initial.png) - frequency graph of modalities alternative to CT, when limited to studies designated as "initial imaging".
  - [filtered_scenarios.xlsx](/output/filtered_scenarios.xlsx) - Excel file containing clinical scenarios in each of the 9 categories of appropriateness by CT or alternative modality. (Note: this should be downloaded locally to open in Excel)
  - [initial_imaging_only_scenarios.xlsx](/output/initial_imaging_only_scenarios.xlsx) - Excel file containing clinical scenarios in each of the 9 categories of appropriateness by CT or alternative modality, when limited to "initial imaging". (Note: this should be downloaded locally to open in Excel)
  