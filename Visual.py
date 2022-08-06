import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


class Visual:

    @staticmethod
    def CreateVisual(self, dataFrame,):
        plt.figure(figsize=(10, 10))
        for i in range(0, dataFrame.shape[0]):
            plt.scatter(dataFrame['Polarity'][i],
                        dataFrame['Subjectivity'][i], color='Pink')
            plt.title("Sentiment Analysis Results")
        plt.xlabel('Polarity')
        plt.ylabel('Subjectivity')
        plt.plot()
        return plt
