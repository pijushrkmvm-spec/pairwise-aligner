# Pairwise Sequence Alignment Tool (Biopython)

This project is a **web-based bioinformatics tool** for performing pairwise sequence alignment using the modern
**PairwiseAligner module from Biopython**.

It allows users to input two sequences and perform **global or local alignment** through a simple web interface.

---

## Features

* Pairwise sequence alignment (global & local)
* Built using Biopython's modern alignment engine
* Flask-based web interface (runs locally)
* Displays:

  * Best alignment
  * Alignment score
  * Aligned regions
* Includes a Jupyter Notebook for learning and experimentation

---

## Project Structure

```
pairwise-aligner/
│
├── app.py                # Flask web application
├── aligner.py            # Core alignment logic
├── requirements.txt      # Dependencies
│
├── templates/
│   └── index.html        # Web interface (GUI)
│
├──static/
|  └── style.css
|
└── notebook/
    └── pairwise_aligner_demo.ipynb   # Learning notebook
```

---

## ⚙️ Requirements

Make sure you have Python installed (3.8+ recommended).

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies include:

* Biopython
* Flask

---

## How to Run the App

1. Clone the repository:

```bash
git clone https://github.com/pijushrkmvm-spec/pairwise-aligner.git
cd pairwise-aligner
```
```GitHub CLI
gh repo clone pijushrkmvm-spec/pairwise-aligner
```

2. Run the application:

```bash
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## How to Use

1. Enter **Query** and **Target** sequences
2. Select alignment mode:

   * Global
   * Local
3. Click **Align**
4. View:

   * Alignment output
   * Score
   * Regions

---

## Notebook (Learning Resource)

The repository includes a Jupyter Notebook demonstrating:

* How PairwiseAligner works
* Different alignment modes
* Scoring system behavior
* Step-by-step experimentation

This is useful for understanding the **underlying logic behind the app**.

---

## Key Concepts

* Pairwise sequence alignment
* Global vs Local alignment
* Scoring systems (match, mismatch, gap penalties)
* Bioinformatics workflow integration

---

## Notes

* This tool uses Biopython’s modern `PairwiseAligner` (not `Pairwise2`)
* The app runs locally (not deployed online)
* Input sequences should be valid nucleotide/protein sequences

---

## Future Improvements

* Alignment visualization (highlight matches/mismatches)
* File upload support (FASTA)
* Parameter tuning (gap penalties, scoring)
* Deployment to cloud (Streamlit / Render)

---

## 👨‍💻 Author

**Pijush Chakraborty**

---

## Acknowledgment

Built using:

* Biopython
* Flask

---

## Final Note

This project demonstrates how bioinformatics algorithms can be integrated into a **usable application pipeline**, combining biological computation with software development.

---

