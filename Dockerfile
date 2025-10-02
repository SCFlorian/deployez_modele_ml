# Utilisation d'une image
FROM python:3.11-slim

# Définition du dossier de travail dans le conteneur
WORKDIR /app

# Copie des fichiers nécessaires
COPY requirements.txt .
COPY api/ ./api/
COPY models/ ./models/

# Installation des dépendances système minimales
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port utilisé par Hugging Face (7860)
EXPOSE 7860

# Lancement de l'API
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "7860"]