
# Import necessary libraries
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Load MNIST dataset from OpenML (you can also use sklearn's inbuilt datasets)
mnist = fetch_openml('mnist_784', version=1)

# Data preprocessing
X = mnist['data'] / 255.0 #Normalize the data (pixels between 0 and 1)
y = mnist['target'].astype(int) #Labels (digits 0-9)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Test accuracy:{accuracy}")

# Display the first 5 test images and their predicted labels
for i in range(5):  # You can change the range to display more images (e.g., 10 or more)
    plt.imshow(X_test.iloc[i].values.reshape(28, 28), cmap=plt.cm.binary)
    plt.title(f"Predicted:{y_pred[i]}, Actual:{y_test.iloc[i]}")
    plt.show()
