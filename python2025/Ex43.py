#Bias and Variance

Import the necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from mlxtend.evaluate import bias_variance_decomp
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
X, y = load_iris(return_X_y=True)

# Split train and test dataset
X_train, X_test,\
    y_train, y_test = train_test_split(X, y,
                                       test_size=0.25,
                                       random_state=23,
                                       shuffle=True,
                                       stratify=y)

# Build the classification model
tree = DecisionTreeClassifier(random_state=123)
clf = BaggingClassifier(base_estimator=tree,
                        n_estimators=50,
                        random_state=23)

# Bias variance decompositions
avg_expected_loss, avg_bias, \
    avg_var = bias_variance_decomp(clf,
                                   X_train, y_train,
                                   X_test, y_test,
                                   loss='0-1_loss',
                                   random_seed=23)
# Print the value
print('Average expected loss: %.2f' % avg_expected_loss)
print('Average bias: %.2f' % avg_bias)
print('Average variance: %.2f' % avg_var)