import streamlit as st
import numpy as np
import joblib

model = joblib. load('decision_tree.pkl')

def main() :
    st.title('FINANCIAL INCLUSION PREDICTION APP')
    st.write('WE WILL HELP YOU PREDICT !')

    COUNTRY = st.number_input('COUNTRY')
    YEAR = st.number_input('YEAR')
    LOCATION_TYPE = st.number_input('LOCATION TYPE')
    cellphone_access = st.number_input('cellphone_access')
    household_size = st.number_input('houschold_size')
    age_of_respondent = st.number_input('age_of_respondent')
    gender_of_respondent = st.number_input('gender_of_respondent')
    relationship_with_head = st.number_input('relationship_with_head')
    marital_status = st.number_input('marital_status')
    education_level = st.number_input('education_level')
    job_type = st.number_input('job_type')

    if st.button( 'Make your prediction : ') :
        features = np.array([[COUNTRY, YEAR ,LOCATION_TYPE ,cellphone_access , household_size ,
                            age_of_respondent , gender_of_respondent , relationship_with_head ,
                            marital_status , education_level , job_type ]])
        result = model.predict(features)
        st.success(result)

    if __name__ == '__main__':
        main()
