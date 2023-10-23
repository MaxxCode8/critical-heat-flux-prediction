import streamlit as st 
import keras
import pickle
import numpy as np 
import time
# load the model ...
model = keras.models.load_model("./model/CHF_FinalMod_.h5")
scaler = pickle.load(open("./model/scaler.pkl", 'rb'))

st.title('🔥🎆 _Critical Heat Flux (Equilibrium) Prediction_ 🎇🔥')

list_of_feats = ['pressure [MPa]', 'mass_flux [kg/m2-s]', 'D_e [mm]', 'D_h [mm]',
       'length [mm]', 'chf_exp [MW/m2]']

def main():
    with st.form(key = "form"):
        # Creating 3 columns for displaying the input parameters
        col1, col2 = st.columns(2)
        
        # each coloumn will have 3 rows each for input parameters
        with col1:
            pressure = st.slider('Pressure [MPa]', 0.1, 21.0, step= 0.01)
            mass_flux = st.slider('Mass Flux [kg/m2-s]', 0.0, 7975.0, 5000.0, step=1.0)
            D_e = st.slider('D_e [mm]', 1.0, 38.0, 11.0, step=0.01)
            
        with col2:
                
            D_h = st.slider('D_h [mm]', 1.0, 120.0, 60.0, step=0.1)
            length = st.slider('Length [mm]', 10.0, 3048.0, 1100.0, step=1.0)
            chf_exp = st.slider('chf_exp [MW/m2]', 0.8, 19.3, 15.0, step=0.1)
        
        submit = st.form_submit_button('Submit Observations')    
    
    if submit:
        # storing the inputs in a numpy array
        inputs = [pressure, mass_flux, D_e, D_h, length, chf_exp]
        inputs = np.array(inputs)
        print(inputs)
        print()
        # scaling the inputs ... We made sure the sequence of the inputs is same as the one used for training
        processed_inputs = scaler.transform(inputs.reshape(1, -1))
        print(processed_inputs)
        # predicting the output
        prediction = model.predict(processed_inputs)
        print()
        print(prediction)    
        print()
        with st.spinner(text='In progress'):
            time.sleep(3)
            st.success('Done')
                # Display the prediction    
            st.write(f'Predicted :red[x_e_out [-]]:fire: Value: _{prediction[0][0]}_') 
            st.write("__*XAI Summary Plot:*__")
            st.image('./xai summary plot.png')
    else:
      st.write("Kindly fill the observations above and then click on the submit button to get the prediction")       

if __name__ == '__main__':
    main()
