
import nltk
from os import getcwd
import w1_unittest

nltk.download('twitter_samples')
nltk.download('stopwords')

filePath = f"{getcwd()}/../tmp2/"
nltk.data.path.append(filePath)
import numpy as np
import pandas as pd
from nltk.corpus import twitter_samples 

from utils import process_tweet, build_freqs
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')


test_pos = all_positive_tweets[4000:]
train_pos = all_positive_tweets[:4000]
test_neg = all_negative_tweets[4000:]
train_neg = all_negative_tweets[:4000]

train_x = train_pos + train_neg 
test_x = test_pos + test_neg

# combine positive and negative labels
train_y = np.append(np.ones((len(train_pos), 1)), np.zeros((len(train_neg), 1)), axis=0)
test_y = np.append(np.ones((len(test_pos), 1)), np.zeros((len(test_neg), 1)), axis=0)

# Print the shape train and test sets
print("train_y.shape = " + str(train_y.shape))
print("test_y.shape = " + str(test_y.shape))
# create frequency dictionary
freqs = build_freqs(train_x, train_y)


print("type(freqs) = " + str(type(freqs)))
print("len(freqs) = " + str(len(freqs.keys())))

# test the function below
print('This is an example of a positive tweet: \n', train_x[0])
print('\nThis is an example of the processed version of the tweet: \n', process_tweet(train_x[0])) # UNQ_C1 GRADED FUNCTION: sigmoid
def sigmoid(z): 
    
   
    h = 1 / (1 + np.exp(-z))

    
    return h # Testing the function 
if (sigmoid(0) == 0.5):
    print('SUCCESS!')
else:
    print('Oops!')

if (sigmoid(4.92) == 0.9927537604041685):
    print('CORRECT!')
else:
    print('Oops again!') # Test the function
w1_unittest.test_sigmoid(sigmoid) 
-1 * (1 - 0) * np.log(1 - 0.9999) 
-1 * np.log(0.0001) # loss is about 9.2
def gradientDescent(x, y, theta, alpha, num_iters):
   
    m = x.shape[0]     
    for i in range(0, num_iters):
        
        z = np.dot(x,theta)
     
        h = sigmoid(z)
       
        J = -1./m * (np.dot(y.transpose(), np.log(h)) + np.dot((1-y).transpose(),np.log(1-h)))                                                    

        theta = theta - (alpha/m) * np.dot(x.transpose(),(h-y))
        
    J = float(J)
    return J, theta

np.random.seed(1)

tmp_X = np.append(np.ones((10, 1)), np.random.rand(10, 2) * 2000, axis=1)

tmp_Y = (np.random.rand(10, 1) > 0.35).astype(float)

tmp_J, tmp_theta = gradientDescent(tmp_X, tmp_Y, np.zeros((3, 1)), 1e-8, 700)
print(f"The cost after training is {tmp_J:.8f}.")
print(f"The resulting vector of weights is {[round(t, 8) for t in np.squeeze(tmp_theta)]}")
def extract_features(tweet, freqs):

    word_l = process_tweet(tweet)
    
    x = np.zeros((1, 3)) 
    

    x[0,0] = 1 
    
    
    for word in word_l:
        
    
        x[0,1] += freqs.get((word, 1.0),0)
        
      
        x[0,2] += freqs.get((word, 0.0),0)
        

    assert(x.shape == (1, 3))
    return x


tmp1 = extract_features(train_x[0], freqs)
print(tmp1)

tmp2 = extract_features('blorb bleeeeb bloooob', freqs)
print(tmp2
    
X = np.zeros((len(train_x), 3))
for i in range(len(train_x)):
    X[i, :]= extract_features(train_x[i], freqs)


Y = train_y

J, theta = gradientDescent(X, Y, np.zeros((3, 1)), 1e-9, 1500)
print(f"The cost after training is {J:.8f}.")
print(f"The resulting vector of weights is {[round(t, 8) for t in np.squeeze(theta)]}")


def predict_tweet(tweet, freqs, theta):
    '''
    Input: 
        tweet: a string
        freqs: a dictionary corresponding to the frequencies of each tuple (word, label)
        theta: (3,1) vector of weights
    Output: 
        y_pred: the probability of a tweet being positive or negative
    '''
    
    x = extract_features(tweet,freqs)

    y_pred = sigmoid(np.dot(x,theta))

    
    return y_pred

for tweet in ['I am happy', 'I am bad', 'this movie should have been great.', 'great', 'great great', 'great great great', 'great great great great']:
    print( '%s -> %f' % (tweet, predict_tweet(tweet, freqs, theta)))

my_tweet = 'I am learning :)'
predict_tweet(my_tweet, freqs, theta) 
def test_logistic_regression(test_x, test_y, freqs, theta):
   
    y_hat = []
    
    for tweet in test_x:
       
        y_pred = predict_tweet(tweet, freqs, theta)
        if y_pred > 0.5:
        
            y_hat.append(1)
        else:
          
            y_hat.append(0)

    
    accuracy = (y_hat==np.squeeze(test_y)).sum()/len(test_x)
    
    return accuracy
tmp_accuracy = test_logistic_regression(test_x, test_y, freqs, theta)
print(f"Logistic regression model's accuracy = {tmp_accuracy:.4f}")
#  error analysis 
print('Label Predicted Tweet')
for x,y in zip(test_x,test_y):
    y_hat = predict_tweet(x, freqs, theta)

    if np.abs(y - (y_hat > 0.5)) > 0:
        print('THE TWEET IS:', x)
        print('THE PROCESSED TWEET IS:', process_tweet(x))
        print('%d\t%0.8f\t%s' % (y, y_hat, ' '.join(process_tweet(x)).encode('ascii', 'ignore'))) 
# Predict 
my_tweet = 'This is a ridiculously bright movie. The plot was terrible and I was sad until the ending!'
print(process_tweet(my_tweet))
y_hat = predict_tweet(my_tweet, freqs, theta)
print(y_hat)
if y_hat > 0.5:
    print('Positive sentiment')
else: 
    print('Negative sentiment')
