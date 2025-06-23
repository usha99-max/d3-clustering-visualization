# Interactive Clustering Visualization using D3.js and Excel Data

This project demonstrates an interactive clustering visualization built using **D3.js** and data parsed from an **Excel spreadsheet** (`.xls`). The goal is to visually explore how vehicles (from the car dataset) group into clusters, and dynamically show insights about those groups.

---

## 📚 Academic Context

> 📝 This project was developed as part of the **Visual Analytics Midterm** in the Master’s in Data Science program. It demonstrates the integration of data parsing, preprocessing, and browser-based interactive visualization using modern JavaScript libraries.

---

## 🎯 Project Objective

- Read data from a `.xls` Excel file (`cars_dataset.xls`)
- Automatically assign rows to four clusters using simple modulo logic (demo purpose)
- Visualize the clusters interactively with:
  - Force-directed node simulation
  - Color-coded groupings
  - Dynamic tooltip for vehicle details
- Display real-time cluster statistics, including the **largest cluster size**

---

## ✨ Features

- ✅ Parses Excel files directly in the browser using `xlsx.js`
- ✅ Generates a **force simulation** of clusters using D3.js
- ✅ Interactive tooltips with car details (Model, MPG, Cylinders, Weight)
- ✅ Nodes can be dragged and repositioned
- ✅ Automatically computes and displays the size of the largest cluster

---

## 💻 Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| `D3.js`      | Data visualization and force simulation |
| `xlsx.js`    | Parsing Excel (.xls) files in-browser |
| `HTML + CSS` | Structuring and styling the page |
| `JavaScript` | Logic for clustering and rendering |

---

## 🗂️ File Structure

MIDTERM/
├── cars_dataset.xls # Input dataset (Excel format)
├── clusteringvisualisation.html # Main HTML + JS visualization
├── converting.py # (Optional) Python script for conversion
├── Midterm Exam.docx # Report document
├── video1619845674.mp4 # Demo video (optional)


---

## 🚀 How to Run

1. Clone or download the repo
2. Open `clusteringvisualisation.html` in your browser
3. Ensure `cars_dataset.xls` is in the same folder
4. The visualization will load and render clusters automatically

---

## 🧠 How Clustering Works (in this version)

> For demonstration purposes, clustering is done using a simple pattern:

```javascript
const clusters = Array.from({ length: 4 }, (_, i) => data.filter((_, j) => j % 4 === i));
