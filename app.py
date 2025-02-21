from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pdfplumber
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
load_dotenv()
def get_gemini_response(input,pdf_content,prompt):
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
    result = llm.invoke([input,pdf_content,prompt])
    return result.content
def pdf_to_text(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
template1 = ''' You are an experienced HR with tech experience in the field of any one job role from Data Science, Full Stack Web Development, Big Data Engineering, DEVOPS, Data Analyst. Your task is to review the provided resume against the job description for these profiles. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements. Resume: {pdf_content}'''
template2 = '''You are an advisor of career development and further skills development towards success in job fields like Data Science, Full Stack Web Development, Big Data Engineering, DEVOPS, Data Analyst. You will tell people how they can get a guaranteed job in the listed fields and provide them with the roadmap they need for improving.'''
template3 = '''You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of job roles like Data Science, Full Stack Web Development, Big Data Engineering, DEVOPS, Data Analyst, and ATS functionality. Your task is to evaluate the resume against the provided job description. Give me the percentage match if the resume matches the job description. First, the output should come as a percentage, then keywords missing, and finally, final thoughts.'''
prompt_template1 = PromptTemplate.from_template(template1)
prompt_template2 = PromptTemplate.from_template(template2)
prompt_template3 = PromptTemplate.from_template(template3)

# Streamlit app
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description:", key="Input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded successfully")

submit1 = st.button("Tell me about the resume")
submit2 = st.button("How can I improvise my skills")
submit3 = st.button("Percentage Match")
if submit1:
    if uploaded_file is not None:
        pdf_content = pdf_to_text(uploaded_file)
        prompt1 = prompt_template1.format(pdf_content=pdf_content, input_text=input_text)
        response = get_gemini_response(prompt1, pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = pdf_to_text(uploaded_file)
        prompt2 = prompt_template2.format(pdf_content=pdf_content, input_text=input_text)
        response = get_gemini_response(prompt2, pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = pdf_to_text(uploaded_file)
        prompt3 = prompt_template3.format(pdf_content=pdf_content, input_text=input_text)
        response = get_gemini_response(prompt3, pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")