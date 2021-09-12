# COVID-19-Pneumonia-Xray-Detector

## Inspiration
Inspiration SARS-COV2 has taken an estimated 4.5 million lives worldwide. With surges, emerging variants, and limited access to vaccine and testing materials, experts agree that the end is not in close reach just yet. In fact, our lives as we know it may have changed indefinitely. Hospitals are forced to cancel surgeries and reserve entire floors for COVID-19 patients, and ICUs are at full capacity across the globe. Today, COVID-19-induced pneumonia is raging through critical care units, and Healthcare providers are facing an immense feeling of burn-out - we aim to ease that burden through Artificial Intelligence based technology. With the aid of qualified radiologists, we hope to outsource our service to reduce costs on care facilities.

## What it does
The goal of our hack is to ease the process of recognizing COVID-19 induced pneumonia, especially in situations where there are time constraints and limited resources for testing - these can quickly become life-or-death moments. Our model inputs radiographic imaging of the chest and outputs the probability that the result is A) COVID-19-induced pneumonia, B) Normal or C) Other Pneumonia. 

## How we built it
We collected chest x-ray data to classify normal, COVID-19 pneumonia and non-COVID pneumonia x-rays. After cleaning and pre-processing the data, we did some data augmentation where we randomly re-scaled, shear zoomed, rotated, and flipped the training set. This way our model was more prepared for real-world tests. After that, we designed a CNN to do a multi-class classification and trained this model for 50 epochs to get 92% accuracy on the test dataset.

## Challenges we ran into
- Data collection: Hard to get chest x-ray of COVID-19 patients
- Training CNN: Requires processing power and time
- Biases that affected our model

## Accomplishments that we're proud of
Apart from completing this hack, we persevered through each challenge as a team and succeeded in what we put ourselves up to. Our team was successfully able to learn about neural networks and make accurate models in a very short amount of time. We were able to achieve high accuracy models (92%) with high precision, recall and f1-score. This shows that our model has fewer false positives and negatives. Today, COVID-19 related development is the most pressing issue at hand, and we recognize the multiple factors that play into the statistics of mortality, recovery, and positive test results. Diagnosis is key, and we truly feel that our hack opens a new door for the research and development as well as the treatment and care of COVID-19 patients.

## What we learned
Through this hack, we took an interdisciplinary approach. With our differing backgrounds in research, coding, app development, hands-on patient care, and public health, we were able to collaborate as a team and learn about topics we were previously unaware of. We applied deep learning skills, project, time, and data management. We uncovered the complexities of COVID-19-induced pneumonia, which opened our eyes to how pressing this matter is.

## What's next for cov-ID
- Expand classification (multi-classification) to further specify the diagnosis
- Train our model with more datasets and for longer epochs to achieve higher accuracy
- Have a more polished interface for users
- Highlight suspected COVID-19 pneumonia markers on the x-ray image
