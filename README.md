# Statistical characterisation of fetal anatomy in simple obstetric ultrasound video sweeps

Repository for statistical characterisation of fetal anatomy in simple obstetric ultrasound video sweeps (https://doi.org/10.1016/j.ultrasmedbio.2024.03.006). Parameters describing statistical heatmaps using video sweeps of the CALOPUS protocol (https://doi.org/10.2196/37374) are provided and made freely available. Parameters exist for fetal presentations: breech, cephalic, transverse and fetal anatomies: head, spine, abdomen, pelvis, femur using 760 unique frame-level manual annotations from 365 unique pregnancies. See first publication provided for more details.

![Summary figure](summary.png)

Two pickle files encode probabilities (probabilities.pkl) and standard deviations (stds.pkl) with the following tree structure:

```
├───A
│   ├───breech
│   │   ├───abdomen
│   │   ├───femur
│   │   ├───head
│   │   ├───pelvis
│   │   └───spine
│   ├───cephalic
│   │   ├───abdomen
│   │   ├───femur
│   │   ├───head
│   │   ├───pelvis
│   │   └───spine
│   └───other
│       ├───abdomen
│       ├───femur
│       ├───head
│       ├───pelvis
│       └───spine
├───B
│   etc ...
```

Step 1 = A \
Step 2 = B \
Step 3 = C \
Step 4 = D \
Step 5 = E \
Following notation given in publication.

**Requirements:** \
numpy \
pickle \
matplotlib

Sample command:
```
python statistical_heatmaps.py
```
Two visualisations should be generated: 1) 1-D detection-based heatmap 2) 2-D line plot with standard deviations visualised as error bars every 5th position. Plots should be identical to those shown on the figure above.

If you use this data in your research, please cite the following paper:
```
@article{gleed2024statistical,
  title={Statistical Characterisation of Fetal Anatomy in Simple Obstetric Ultrasound Video Sweeps},
  author={Gleed, Alexander D and Mishra, Divyanshu and Self, Alice and Thiruvengadam, Ramachandran and Desiraju, Bapu Koundinya and Bhatnagar, Shinjini and Papageorghiou, Aris T and Noble, J Alison},
  journal={Ultrasound in Medicine \& Biology},
  volume={50},
  number={7},
  pages={985--993},
  year={2024},
  publisher={Elsevier}
}
```
