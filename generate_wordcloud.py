from typing import Dict

import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_wc(words: Dict[str, int]):
    """Generate a word cloud from a weighted collection of words
    
    Args:
        words (Dict[str, int]): Dictionary mapping words to their respective weight.
                                Weight indicates size in word cloud.
    """
    # Generate text containing words with occurances
    #text = []
    #for word, repetitions in words.items():
    #    text.extend([word] * repetitions)
    #text = ' '.join(text)

    # Construct word cloud
    wc = WordCloud(max_font_size=50, background_color="white", width=1200, height=300)
    wc_img = wc.generate_from_frequencies(words)
    wc_img.to_file("images/interests.png")

    # Display word cloud
    plt.imshow(wc_img, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    generate_wc({
        'Machine Learning': 6,
        'Deep Learning': 5,
        'Computer Vision': 5,
        'Pytorch': 5,
        'Data Science': 4,
        'Research': 4,
        'NLP': 4,
        'Data Analysis': 4,
        'NLP': 4,
        'Self-Supervision': 4,
        'AI': 3,
        'Point Clouds': 3,
        'Autonomous Driving': 3,
        'Few-Shot Learning': 3,
        'Pandas': 3,
        'Scikit-Learn': 3,
        'Python': 3,
        'Robustness': 2,
        'PySpark': 2,
        'Git': 2,
        'Docker': 2,
        'Signal Processing': 1,
        'Linux': 1,
        'CI/CD': 1,
    })