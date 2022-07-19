# adult-classification

## Summary

*  Implementation of a end to end ML project for a **binary classification** dataset with a **mild imbalance** (23 %). 
*  The [Adult-Income dataset](https://archive.ics.uci.edu/ml/datasets/adult) relates salaries with an array of socioeconomic indicators in the U.S.
*  A **logistic** and **gradient boosting** models has been tested in addition with the algorithm **SMOTE** for increasing the **recall** in the positive class.
* **AUC-ROC of 0.85** in a 10-fold cross-validation with the full dataset (30k+ obs)
* The final model is available through a **dockerised Flask API REST** endpoint.

## Deploying model

In a bash terminal inside the proyect folder, the following command will [compile and run](https://stackoverflow.com/questions/45141402/build-and-run-dockerfile-with-one-command) the docker image hosting the REST API server, listening for new examples queries to infer: 
```{bash}
cd production
docker run --rm -it $(docker build -q .)
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

## Improvements
- Include more models: naive bayes, svm, mlp
- Feature selection to reduce computation time & simplicity.
- Feature importance explainer
- Extend API code for batch inference

## Sources 

- https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/
- https://scikit-learn.org/stable/tutorial/statistical_inference/putting_together.html
- https://machinelearningmastery.com/hyperparameters-for-classification-machine-learning-algorithms/
- https://www.kaggle.com/code/namanmanchanda/heart-attack-eda-prediction-90-accuracy
- https://archive.ics.uci.edu/ml/datasets/adult
- https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/#:~:text=Perhaps%20the%20most%20common%20metric,more%20generally%20as%20cross%2Dentropy.
