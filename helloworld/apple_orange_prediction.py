

APPLE_SHAPE = 0
ORANGE_SHAPE = 1

LABEL_APPLE = 0
LABEL_ORANGE = 1

from sklearn import tree


def get_data():
    X = [[150, APPLE_SHAPE], [160, APPLE_SHAPE], [120, ORANGE_SHAPE], [135, ORANGE_SHAPE]]
    Y = [LABEL_APPLE, LABEL_APPLE, LABEL_ORANGE, LABEL_ORANGE]
    return (X, Y)

def analyze(x, y):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)
    return clf
    
def predict(clf, x, y):    
    prediction = clf.predict([[x, y]])
    if prediction == 1:
        print("It's an ORANGE")
    elif prediction == 0:
        print("It's an APPLE")
    else:
        print("I don't this fruit")
        
        
if __name__ == "__main__":
    x, y = get_data()
    clf = analyze(x, y)
    predict(clf, 100, 0)