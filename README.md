# End-to-End-Fashion-Recommendation-System-with-MLOps

# 👔 Fashion Recommendation System (End-to-End ML Project)

## 📌 Problem Statement

In today’s generation, especially among **Gen Z male audiences**, fashion is not just about clothing — it is a form of **self-expression, identity, and social presence**.

However:

* Many users struggle to choose outfits that match their style
* Lack of personalized recommendations
* Overwhelming number of options in online platforms

👉 **Goal:** Build an intelligent system that recommends fashion items based on user preferences using a **content-based recommendation approach**, solving the **cold-start problem**.

---

## 💡 Solution Overview

This project implements an **End-to-End Fashion Recommendation System** that:

* Extracts meaningful features from fashion products
* Uses TF-IDF + Cosine Similarity for recommendations
* Provides suggestions even for new users (cold start)
* Deploys a fully automated pipeline with MLOps practices

---

## 🧠 Why Recommendation System?

### ✅ Cold Start Advantage

Unlike collaborative filtering:

* Does NOT depend on user history
* Works effectively for:

  * New users
  * New products

👉 This makes it ideal for real-world fashion platforms.


## 🏗️ System Architecture

<img width="1301" height="740" alt="Image" src="https://github.com/user-attachments/assets/cf5fa61b-ee6e-4507-a900-88ff8514e6ae" />

Data Collection → Data Validation → Data Transformation
        ↓
Feature Engineering → Model Building → Model Evaluation
        ↓
API Development → Deployment → CI/CD Pipeline

---

## ⚙️ Pipeline Explanation

### 1. Data Collection

* Gather fashion product data (descriptions, categories, etc.)

### 2. Data Validation

* Ensure data quality and consistency

### 3. Data Transformation

* Clean and preprocess text data

### 4. Feature Engineering

* Convert text into numerical form using TF-IDF

### 5. Model Building

* Apply Cosine Similarity to find similar products

### 6. Model Evaluation

* Validate recommendation relevance

### 7. API Development

* Build API using FastAPI / Flask

### 8. Deployment

* Containerize using Docker and deploy to AWS

### 9. CI/CD Pipeline

* Automate workflow using GitHub Actions

---

## 🛠️ Tech Stack

* Python
* scikit-learn
* Visual Studio Code
* MLflow
* DagsHub
* Docker
* GitHub Actions
* Amazon Web Services (AWS)
# Tools used

<img width="225" height="225" alt="Image" src="https://github.com/user-attachments/assets/42befdbc-45c6-4a5a-a4f3-38d8afad0413" />

<img width="306" height="165" alt="Image" src="https://github.com/user-attachments/assets/79a51636-fbda-48d1-86cf-2f8bb76ac3da" />

<img width="231" height="218" alt="Image" src="https://github.com/user-attachments/assets/0fba3b61-ffca-474f-85c2-cc16c748bc49" />

<img width="343" height="147" alt="Image" src="https://github.com/user-attachments/assets/5751eaf2-b981-47c7-b63c-45e144b06235" />

<img width="318" height="159" alt="Image" src="https://github.com/user-attachments/assets/e11a38e3-8062-4573-aab3-263dd1946c11" />


## 🚀 How to Run the Project (Using Docker)

### 🔹 Step 1: Pull Docker Image

```
docker pull samdocker4/fashion-recommendation-system:latest
```

### 🔹 Step 2: Run the Container

```
docker run -p 5000:5000 -p 5801:5801 samdocker4/fashion-recommendation-system:latest
```

### 🔹 Step 3: Access Application

```
http://localhost:5000
```

---

## 📦 Project Highlights

* End-to-End ML Pipeline
* Solves Cold Start Problem
* MLOps Integrated (CI/CD + Tracking)
* Dockerized & Cloud Deployed
* Scalable Architecture

---

## 📌 Future Improvements

* Add deep learning-based recommendations
* Integrate user personalization
* Build UI for better experience
* Add real-time recommendations

---

## 🙌 Conclusion

This project demonstrates how **data science + MLOps** can be combined to build a **real-world scalable recommendation system**, especially relevant for modern fashion trends and Gen Z users.
