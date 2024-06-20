# ThOP - Experiments & Visualization
<div style="text-align: center;">
    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjVwanRka25zbGU3ZDB3cDVveGF1c2lpemx6bGpkcXR0dDh2encyNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aKmpdeSkymMtILVDCK/giphy.gif" alt="Thief Orienteering Problem Visualization Tool">
</div>
<p align="center"> 
    <a aria-label="Thopvis is free to use" href="/LICENSE" target="_blank">
        <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-success.svg?style=flat-square&color=33CC12" target="_blank" />
    </a>
</p>

---
A tool that enables users to view details and execute any thop instances.
## Disclaimer
The algorithms and experimental methods used in this repository are derived from [acoplusplus](https://github.com/jonatasbcchagas/acoplusplus_thop) and the paper [Efficiently solving the thief orienteering problem with a max-min ant colony optimization algorithm](https://link.springer.com/article/10.1007/s11590-021-01824-y).

I am in no way associated with Jonatas B. C. Chagas and Markus Wagner.

## Usage
You can find the visualization tool `thopvis` in the `thop_visualiser` directory.

You may also need to install some Python dependencies to run the visualizer:

```shell
pip install tk tkscrolledframe matplotlib
```
To start the visualizer, simply run the following commands:

```shell
cd thop_visualiser
python thopvis.py
```

**Note**: This tool was previously designed to run solely on Linux, but it can still load and run the existing `eil51-thop` instances on Windows.

---
<p align="center">Dev-Aligator</p>
<p align="center">
<a href="https://github.com/Dev-Aligator/">
<img src="https://user-images.githubusercontent.com/58631762/120077716-60cded80-c0c9-11eb-983d-80dfa5862d8a.png" width="19">
</a>