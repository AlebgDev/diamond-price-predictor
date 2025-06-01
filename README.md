# 💎 Diamond Price Predictor

Proyecto de aprendizaje automático para predecir el precio de diamantes a partir de sus características físicas y cualitativas.

---

## 🎯 Objetivo

Este repositorio contiene un sistema de Machine Learning que predice el precio de diamantes utilizando variables como peso (`carat`), claridad (`clarity`), corte (`cut`), color, y dimensiones físicas (`x`, `y`, `z`).

Este proyecto fue elaborado como parte de una competencia académica en CEUPE (Big Data & Analytics).

---

## 📁 Estructura del Proyecto

diamond-price-predictor/
├── data/ # Datos originales y de prueba
├── notebooks/ # Análisis y modelado en Jupyter/Colab
├── src/ # Funciones reutilizables
├── outputs/ # Resultados del modelo
├── requirements.txt # Dependencias del entorno
└── README.md # Este archivo

## 🔍 EDA (Exploratory Data Analysis)

El análisis exploratorio incluye:

- Distribuciones de variables numéricas y categóricas
- Relación entre carat y price
- Matriz de correlación
- Boxplots por `cut`, `color`, `clarity`
- Detección de outliers en dimensiones físicas

---

## 🧠 Modelo

- **Modelo usado:** `RandomForestRegressor` de `scikit-learn`
- **Métrica:** RMSE (Root Mean Squared Error)
- **Técnicas aplicadas:**
  - One-hot encoding para variables categóricas
  - Limpieza de datos (`x`, `y`, `z` = 0 eliminados)
  - Alineación de columnas entre train y test

---