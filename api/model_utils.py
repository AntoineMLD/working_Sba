from joblib import load

# Fonction pour charger un modèle à partir d'un fichier .pkl.
def load_model(path='modele_usba.pkl'):
    # La fonction load de joblib est utilisée pour charger le modèle.
    model = load(path)
    # Le modèle chargé est retourné.
    return model

# Fonction pour faire des prédictions avec un modèle donné sur des données fournies.
def prediction(model, data):
    # Le modèle est utilisé pour faire des prédictions sur les données.
    predictions = model.predict(data)
    # Les prédictions sont retournées.
    return predictions
