from sklearn.datasets import load_digits
import pandas as pd
import matplotlib.pyplot as plt
digits = load_digits()
print(digits.data[0])
plt.gray()
plt.matshow(digits.images[0])
plt.show()