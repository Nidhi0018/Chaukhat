<div align="center">
  <img src="static/download (2).jpeg" width="100%" alt="Chaukhat Banner">
  
  <br>

  ## $\color{#2b5968}{\textsf{Welcome to Chaukhat: The Gateway to Your Future}}$
  <p><i>"Because a home is not just a coordinate; it is a new chapter."</i></p>

  ### [🏠 Live Application](https://chaukhat-dgj6athq78ubgvod8peufy.streamlit.app/) | [📁 Project Repository](https://github.com/Nidhi0018/Chaukhat)
</div>

---

### $\color{#97b5c2}{\textsf{🏡 The Vision: Why Chaukhat?}}$
In many traditions, the **Chaukhat** (doorstep) is the sacred boundary between the outer world and the sanctuary of a home. Transitioning through a Chaukhat marks one of life's most significant milestones. 

Most real estate tools are cold, clinical, and data-heavy. **Chaukhat** was created to humanize the process. It bridges the gap between complex Machine Learning and the emotional journey of home-buying by providing a **"Trusted Reflection"** of market value within an immersive, heritage-inspired environment.

### $\color{#dfc2c0}{\textsf{✨ Immersive User Experience (UX)}}$
* **$\color{#2b5968}{\textsf{Cinematic Entrance:}}$** A full-screen splash screen featuring a traditional ornamental door, recreating the feeling of a "Ghar Pravesh" (Home Entrance).
* **$\color{#2b5968}{\textsf{Heritage Aesthetics:}}$** A specialized UI featuring ornamental motifs and a soft **Pearl Pink** and **Slate Blue** palette to reduce cognitive load and "data fatigue."
* **$\color{#2b5968}{\textsf{Human-Centric Inputs:}}$** Instead of rigid technical labels, inputs are framed around family comfort, such as asking for *"Room to Grow"* to determine space requirements.

### $\color{#97b5c2}{\textsf{🧠 The AI Brain: Random Forest Regressor}}$
**What is this project doing?**
The core objective is to predict property prices by analyzing multi-dimensional factors like location popularity, total area, and amenities.

**Why Random Forest?**
We chose the **Random Forest Regressor** over other models (like Linear Regression or Simple Decision Trees) for several critical reasons:
1. **Handling Non-Linearity:** Real estate prices don't increase "linearly." A house in a prime location might be 10x more expensive than one just a few miles away. Random Forest excels at capturing these non-linear jumps.
2. **Robustness to Outliers:** Real estate data often contains "luxury outliers." Random Forest, being an ensemble of many trees, is less likely to be skewed by a single overpriced mansion.
3. **Preventing Overfitting:** By averaging the results of multiple decision trees, the model generalizes better to new, unseen houses compared to a single complex tree.
4. **Feature Importance:** It allows us to understand which factors (like location vs. square footage) are driving the price, aligning with our goal of **Explainable AI**.

### $\color{#dfc2c0}{\textsf{🛠️ Technical Architecture}}$
* **$\color{#2b5968}{\textsf{Frontend:}}$** [Streamlit](https://streamlit.io/) with custom CSS/HTML injection for brand identity.
* **$\color{#2b5968}{\textsf{Backend:}}$** Python-based inference engine.
* **$\color{#2b5968}{\textsf{Model Persistence:}}$** Serialized using `pickle` for instant loading and prediction.
* **$\color{#2b5968}{\textsf{Cloud Infrastructure:}}$** Hosted on Streamlit Community Cloud with automated CI/CD.

### $\color{#97b5c2}{\textsf{📂 Project Structure}}$
```text
├── app.py                # UI Logic & Branding
├── RF_model.pkl          # Trained Random Forest Model
├── classes.npy           # Encoded Location Labels
├── cleaned_df.csv        # Reference Dataset
├── requirements.txt      # Dependency Manifest
└── static/               # Visual Assets (Door, Interior, Motifs)
