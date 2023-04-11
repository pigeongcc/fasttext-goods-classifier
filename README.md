# Multiclass Goods Classificator

This is a summary of the solution notebook.

Details are covered in the notebook.

## Solution Steps

- Exploratory data analysis

- Oversampling of rare classes up to 50+ samples each. Increased the score for 0.05

- Feature engineering:
    
    - Target encoding for `shop_id` categorical feature. Did not lead to a score increase.

    - Dropping of `rating` and `sale` features.

- Textual features processing:

    - Removing of punctuation, stop-words, digits, emojis.

    - Lemmatization.

    - Vectorization with fastText.

- Stratified train-valid-test split.

- Hyperparameter search with Optuna

- Training a MLP on obtained embeddings.


## Space for Improvement

- To use images. Build images representations, e.g. with fine-tuned CNN.

- To add embeddings from other vectorizers, e.g. BERT.

- To implement cross-modal representation of images and textual data.