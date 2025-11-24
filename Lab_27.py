# import numpy as np
# import seaborn as sns
# sns.set(style="white")
# # Generate a random univariate dataset
# rs = np.random.RandomState(10)
# d = rs.normal(size=100)
# # Plot a simple histogram and kde
# sns.histplot(d, kde=True, color="m")


import seaborn as sns
sns.set(style="dark")
fmri = sns.load_dataset("fmri")
# Plot the responses for different\
# events and regions
sns.lineplot(x="timepoint",
             y="signal",
             hue="region",
             style="event",
             data=fmri)
