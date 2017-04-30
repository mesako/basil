
import matplotlib.pyplot as plt

def plot_categories_pie_chat(summary_stats_df):
    labels = list(summary_stats_df.index.values)
    sizes = list(summary_stats_df["Relative Percent"])
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, autopct = '%1.0f%%',
            shadow = False, startangle = 90)
    ax1.axis('equal')
    plt.show()

