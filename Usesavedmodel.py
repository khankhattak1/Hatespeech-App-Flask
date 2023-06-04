#Import Dependies
import tensorflow as tf
import pandas as pd
import os
import re
from keras.layers import TextVectorization    


def score_comment(comment):
    # Load model
    model = tf.keras.models.load_model('toxicity.h5')

    # Using text Vectorizer
    df = pd.read_csv(os.path.join('Ethos_MultiTarget','train.csv', 'train.csv'))
    X = df['comment_text']


    MAX_FEATURES = 200000
    vectorizer = TextVectorization(max_tokens = MAX_FEATURES, 
                            output_sequence_length=1800,
                            output_mode='int')
    vectorizer.adapt(X.values)

    # Label Function

    vectorized_comment = vectorizer([comment])
    results = model.predict(vectorized_comment)
    
    text = ''
    for idx, col in enumerate(df.columns[2:]):
        text += '{}: {}\n\t'.format(col, results[0][idx]>0.5)

    return text

print(score_comment('This is a test'))