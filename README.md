# 💻 AI-Powered Laptop Recommendation System

This is an intelligent **Laptop Recommendation System** built using **Streamlit**, **scikit-learn**, and **Pandas**. The system uses **cosine similarity** on encoded and normalized laptop features to suggest laptops similar to a selected model.

---

## 🎯 Features

- 🔎 **Search bar** to search for a laptop model by name.
- ✅ **Dropdown selector** to choose a specific laptop.
- 📈 **AI-powered recommendations** based on:
  - Brand
  - Processor
  - GPU
  - RAM size
  - Memory size
  - Number of cores
  - Rating
  - Price
- 📊 Results displayed in a user-friendly table.
- ⚠️ Warns users if no laptops are found based on their search.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web UI
- [scikit-learn](https://scikit-learn.org/) – Cosine similarity, preprocessing
- [Pandas](https://pandas.pydata.org/) – Data handling
- [NumPy](https://numpy.org/) – Numeric operations

---

## 📂 Dataset Requirements

The app expects a CSV file named **`laptops.csv`** containing the following columns:

| Column Name      | Description                     |
|------------------|---------------------------------|
| model            | Laptop model name (string)      |
| brand_name       | Brand of the laptop             |
| processor_brand  | Processor brand (e.g., Intel)   |
| gpu_brand        | GPU brand (e.g., NVIDIA)        |
| os               | Operating system (e.g., Windows)|
| ram_num          | RAM in GB (numeric)             |
| memory_size      | Storage size in GB              |
| core_num         | Number of CPU cores             |
| rating           | Average user rating (out of 5)  |
| price            | Laptop price in INR             |

Ensure that the dataset has clean and consistent values for accurate recommendations.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai-laptop-recommender.git
   cd ai-laptop-recommender

📌 Example:
+--------------------------+
| 📌 Recommended Laptops   |
+--------------------------+
| Dell Inspiron 15         |
| HP Pavilion x360         |
| Lenovo IdeaPad Slim 5    |
| ASUS VivoBook Ultra      |
| Acer Aspire 7            |
+--------------------------+

