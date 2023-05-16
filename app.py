import streamlit as st 
import joblib
import numpy as np


 



def main():
    
       
    model = joblib.load('matriosca.pkl')
    
    crim = st.number_input('input1',0,10,5)
    zn = st.number_input('input2',0,10,5)
    indus = st.number_input('input3',0,10,5)
    chas = st.number_input('input4',0,10,5)
    nox = st.number_input('input5',0,10,5)
    rm = st.number_input('input6',0,10,5)
    age = st.number_input('input7',0,10,5)
    dis= st.number_input('input8',0,10,5)
    rad = st.number_input('input9',0,10,5)
    tax = st.number_input('input10',0,10,5)
    ptratio = st.number_input('input11',0,10,5)
    b = st.number_input('input12',0,10,5)
    Istat = st.number_input('input13',0,10,5)
    arr = np.array([[crim, zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,Istat]])
    res= model.predict(arr)
    st.write(f"Risultato: {res}")
        
        # buffer = io.BytesIO()
        # # download button 2 to download dataframe as xlsx
        # with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        #     # Write each dataframe to a different worksheet.
        #     df.to_excel(writer, sheet_name='Sheet1', index=False)
        #     # Close the Pandas Excel writer and output the Excel file to the buffer
        #     writer.save()

        #     download2 = st.download_button(
        #         label="Download data as Excel",
        #         data=buffer,
        #         file_name='large_df.xlsx',
        #         mime='application/vnd.ms-excel')
        
if __name__=="__main__":
    main()
