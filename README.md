# adult-classification



# Deploying model

In a bash terminal inside the proyect folder 
```{bash}
cd production
docker run -it $(docker build -q .)
```

Example query: 

```{bash}
curl http://172.17.0.2:5000/getPrediction -H "Content-Type: application/json" -d '{
    "age": [39],
    "workclass": ["State-gov"],
    "fnlwgt": [77516],
    "education": ["Bachelors"],
    "education-num": [13],
    "marital-status": ["Never-married"],
    "occupation": ["Adm-clerical"],
    "relationship": ["Not-in-family"],
    "race": ["White"],
    "sex": ["Male"],
    "capital-gain": [2174],
    "capital-loss": [0],
    "hours-per-week": [40],
    "native-country":["United-States"]
}'
```

```{bash}
{"data":[0]}
```


## Sources 

- https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/
- https://scikit-learn.org/stable/tutorial/statistical_inference/putting_together.html
- https://machinelearningmastery.com/hyperparameters-for-classification-machine-learning-algorithms/
- https://www.kaggle.com/code/namanmanchanda/heart-attack-eda-prediction-90-accuracy
- https://archive.ics.uci.edu/ml/datasets/adult
- https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/#:~:text=Perhaps%20the%20most%20common%20metric,more%20generally%20as%20cross%2Dentropy.
