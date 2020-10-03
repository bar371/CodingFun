import pandas as pd
import numpy as np
from sklearn.cross_validation import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFECV
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns




if __name__ == '__main__':
    cmap = sns.diverging_palette(5, 250, as_cmap=True)


    def magnify():
        return [dict(selector="th",
                     props=[("font-size", "7pt")]),
                dict(selector="td",
                     props=[('padding', "0em 0em")]),
                dict(selector="th:hover",
                     props=[("font-size", "12pt")]),
                dict(selector="tr:hover td:hover",
                     props=[('max-width', '200px'),
                            ('font-size', '12pt')])
                ]


    corr.style.background_gradient(cmap, axis=1) \
        .set_properties(**{'max-width': '80px', 'font-size': '10pt'}) \
        .set_caption("Hover to magify") \
        .set_precision(2) \
        .set_table_styles(magnify())
    reviews = pd.read_csv("text_training.csv")
    print(reviews)

    #
    # #print(reviews.head(5))
    #
    # # y = pd.get_dummies(reviews['rating'])
    # X = reviews[reviews.columns[1:-1]]
    # y = reviews['rating'].values
    #
    # # print(X)
    # # print(y)
    # logits = LogisticRegression(random_state=0)
    # # logits.fit(X,y)
    #
    # rfecv = RFECV(estimator=logits, cv=10)
    # rfecv = rfecv.fit(X,y)
    # # ret = rfecv.transform(X, y)
    # # print(ret)
    # print("Optimal number of features : %d" % rfecv.n_features_)
    # print (rfecv.support_)
    # # features=X[:,rfecv.support_]
    # # Plot number of features VS. cross-validation scores
    # plt.figure()
    # plt.xlabel("Number of features selected")
    # plt.ylabel("Cross validation score (nb of correct classifications)")
    # plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
    # plt.show()