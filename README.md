# Applied Machine Learning (Cornell CS5785, Fall 2024)

This repo contains executable course notes and slides for the Applied ML course at Cornell and Cornell Tech (Fall 2024 edition).

Note that these notes are slightly different from the ones used in my Youtube [lecture videos](https://www.youtube.com/watch?v=vcE9WGbi4QY&list=PL2UML_KCiC0UlY7iCQDSiGDMovaupqc83) videos from the Fall 2020 edition of the course. You may find these in my other Github repo.

## Contents

This repo is organized as follows.

```
.
├── README.md
├── slides                # Course slides
├── lecture-notes         # Lecture notes (expanding on the material in the slides)
└── requirements.txt      # Packages needed for your virtualenv
```

## Tentative Schedule
[PDFs of the slides](https://drive.google.com/drive/folders/1-M6tNLGOMa4erAMj31jwmm-6m2MK0Prw?usp=sharing) —
please check back before the lectures as we will be updating the slides and PDFs throughout the semester.

| Date | Lecture |
|------|---------|
| **8/26/2024** | [Introduction: Supervised, unsupervised, reinforcement learning](./slides/lecture01-introduction.ipynb) |
| **8/28/2024** | In-Class Tutorial: Linear Algebra, Probability |
| **9/4/2024** | [SL] [Introduction. Models, features, objectives, optimization](./slides/lecture02-supervised-learning.ipynb) |
| **9/9/2024** | [SL] [Regression. Linear Regression. OLS](./slides/lecture03-linear-regression.ipynb) |
| **9/11/2024** | [SL] [Classification. Logistic Regression and Max Likelihood](./slides/lecture04-classification.ipynb) |
| **9/16/2024** | [SL] [Why Does SL Work? Data distribution, over/under fitting, regularization](./slides/lecture05-regularization.ipynb) |
| **9/18/2024** | [SL] [Naive Bayes. Bag of words](./slides/lecture06-naive-bayes.ipynb) |
| **9/23/2024** | [SL] [Generative vs. discriminative methods](./slides/lecture07-gaussian-discriminant-analysis.ipynb) |
| **9/25/2024** | Guest Lecture |
| **9/30/2024** | [UL] [Introduction to Unsupervised Learning. K-Means](./slides/lecture09-unsupervised-learning.ipynb) |
| **10/2/2024** | [UL] [Clustering. Gaussian mixture models, expectation-maximization](./slides/lecture08-clustering.ipynb) |
| **10/7/2024** | [UL] [Dimensionality Reduction. PCA](./slides/lecture10-dimensionality-reduction.ipynb) |
| **10/9/2024** | (UL) Visualization. PCA vs. TSNE |
| **10/14/2024** | Fall Break - No class |
| **10/16/2024** | [SL] [SVMs. Margins, max-margin classifiers, hinge loss, optimization](./slides/lecture12-suppor-vector-machines.ipynb) |
| **10/21/2024** | [SL] [Dual Formulation of SVMs. Lagrange duality, SVMs duals, SMO](./slides/lecture13-svm-dual.ipynb) |
| **10/23/2024** | [SL] [Kernels. Kernel trick, examples of kernels, Mercer's theorem](./slides/lecture14-kernels.ipynb) |
| **10/28/2024** | [Prelim Review](./slides/lecture15-midterm-review.ipynb) |
| **10/30/2024** | Prelim In Class |
| **11/4/2024** | [SL] [Neural Networks. Perceptrons, multi-layer neural networks](./slides/lecture16-neural-networks.ipynb) |
| **11/6/2024** | [SL] [Deep Learning. Convolutional neural networks and applications](./slides/lecture17-deep-learning.ipynb) |
| **11/11/2024** | (SL) Advanced Deep Learning. ResNets, RNNs |
| **11/13/2024** | (SL) Advanced Deep Learning. Transformers/LLMs |
| **11/18/2024** | [SL] [Decision Trees. Bagging, ensembling, CART](./slides/lecture20-decision-trees.ipynb) |
| **11/20/2024** | [SL] [Boosting. Adaboost, gradient boosting](./slides/lecture21-boosting.ipynb) |
| **11/25/2024** | Guest Lecture |
| **11/27/2024** | Thanksgiving Break - No class |
| **12/2/2024** | Machine Learning: Diagnosis. Model iteration process, bias/variance tradeoff, baselines, learning curves |
| **12/4/2024** | Applying Machine Learning: Diagnosis. Error analysis, data integrity, human-level performance |
| **12/9/2024** | [Final Lecture. Overview of the course. Taxonomy of ML algorithms. Research directions](./slides/lecture24-overview.ipynb) |

## Setup

### Requirements

You should be able to run all the contents of this repo using the packages provided in `requirements.txt`.

In a new `virtualenv`, run this:
```
pip install -r requirements.txt
```

## Feedback

Please send feedback to [Volodymyr Kuleshov](https://www.cs.cornell.edu/~kuleshov/)
