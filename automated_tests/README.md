# Automated Tests

This program will run RoboCup Soccer Simulation 2D League matches. You will need rcssserver, rcssmonitor and the teams installed in your computer. 

Modify the specific shell files to adapt to your system.

Run locally:

```console
git clone https://github.com/ibotsuft/scripts.git --branch main --single-branch automated_tests
```

Create a virtual environment:
```console
python -m venv venv/
```

Activate environment:
```console
.\venv\Scripts\Activate.ps1
```
Others ways to activate environment: https://docs.python.org/3/library/venv.html#how-venvs-work


Install dependencies:
```console
pip install -r requirements.txt
```