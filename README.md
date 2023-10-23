# Critical Heat Flux Detection 🔥🎆🎇
### A scratch-2-deployment ml side project ( with GCP app engine Deployment )
---
This dataset was prepared for the journal article entitled "On the prediction of critical heat flux using a physics-informed machine learning-aided framework" (doi: 10.1016/j.applthermaleng.2019.114540). The dataset contains processed and compiled records of experimental critical heat flux and boundary conditions used for the work presented in the article.

The critical heat flux (CHF) corresponding to the departure from nucleate boiling (DNB) crisis is essential to the design and safety of a two-phase flow boiling system. Despite the abundance of predictive tools available to the thermal engineering community, the path for an accurate, robust CHF model remains elusive due to lack of consensus on the DNB triggering mechanism. This work aims to apply a physics-informed machine learning (ML)-aided hybrid framework to achieve superior predictive capabilities. Such a hybrid approach takes advantage of existing understanding in the field of interest (i.e., domain knowledge) and uses ML to capture undiscovered information from the mismatch between the actual and domain knowledge-predicted target.

The reliability and economic competitiveness of a thermal system hinge upon its safety and regulatory measures. During the stage of system design and analysis, researchers and engineers typically leverage extensive experimental efforts and investigate evolutionary models that represent the state-of-the-art understanding in their fields of specialization—also known as *domain knowledge* (DK)—to predict various safety limits.

🧭**Problem Statement:** The target feature is **x_e_out** which is a continuous variable. The scoring metric is **RMSE**. 

---
*Here are some photos if you are not a fan of reading :)*<br>
![deploy image streamlit1](https://github.com/MaxxCode8/critical-heat-flux-prediction/assets/105921273/ee246c47-e3b4-49ee-8a59-3f5204a496eb)
![deploy image streamlit2](https://github.com/MaxxCode8/critical-heat-flux-prediction/assets/105921273/61bbddc9-b040-4cac-b662-e30183ce1201)

---
*Gcp App Engine Usage Statistics* <br>
![Summary app engine usage](https://github.com/MaxxCode8/critical-heat-flux-prediction/assets/105921273/7b5824cb-3017-4270-825f-a6efe3a28495)

---
<span style="font-size:35px"><b>                                  The Flow in which the project happened:</b></span>

<span style="font-size:30px"><b><i>Get Dataset</i></b></span><br>
<p>        ⬇</p>
<p>        ⬇</p>
<span style="font-size:30px"><b><i>JupyterNB (Baseline Model.ipynb)</i></b></span><br>
<br>
<p>        ⬇</p>
<p>        ⬇</p>
<span style="font-size:30px"><b><i>Streamlit (app.py)</i></b></span> <br>
<br>
<p>        ⬇</p>
<p>        ⬇</p>
<span style="font-size:30px"><b><i>Dockerfile & app.yaml (GCP app engine config)</i></b></span> <br>
<br>
<p>        ⬇</p>
<p>        ⬇</p>
<span style="font-size:30px"><b><i>Google Cloud SDK (Deploy)</i></b></span>

---
## References:
AndrewNG and "the Internet" helped me get an understanding of ML and AI... Consistency and Passion is the Key 🔑<br>
[Streamlit Docs](https://docs.streamlit.io/) | [Streamlit Syntax CheatSheet](https://docs.streamlit.io/library/cheatsheet) <br>
[App Engine Docs](https://cloud.google.com/build/docs/deploying-builds/deploy-appengine) <br>
[One of many Youtube Videos I Reffered for App Engine deployment](https://youtu.be/03KgXhg-voY?si=jKImhdyMI3-Ogpi5) <br>
*you can also search for articles and other videos and just try sticking to one of them till the end!* <br>
PS: There are multiple ways to deploy an app on GCP, for *simplicity's sake* I have chosen the App Engine way.

---
Note: The Dataset and Problem Statement was provided as a Part of [TMLC-MGP](https://themlco.com/academy/mgp/) 🙏 <br>
___Happy Learning!___
