# Import necessary libraries
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Load MNIST dataset from OpenML (you can also use sklearn's inbuilt datasets)
mnist = fetch_openml('mnist_784', version=1)

# Data preprocessing


# Split into training and test sets


# Create and train a logistic regression model


# Evaluate the model


# Display the first 5 test images and their predicted labels
  # You can change the range to display more images (e.g., 10 or more)


