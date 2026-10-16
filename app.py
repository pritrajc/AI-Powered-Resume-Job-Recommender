import streamlit as st
from src.helper import extract_text_from_pdf, ask_ollama
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

st.set_page_config(page_title ="Job Recommender",layout="wide")
st.title("AI Job Recommender")
st.markdown("Upload your resume and get job recomendation based on your skill and experiences")

uploaded_file = st.file_uploader("Upload you resume (PDF)", type=["pdf"])

if uploaded_file:
  with st.spinner("Extract text from resume..."):
    resume_text = extract_text_from_pdf(uploaded_file)

  with st.spinner("summarizing your resume"):
    summary = ask_ollama(f"Summarize this resume highlighting the skill, education, and experience: \n\n{resume_text}",max_tokens=500,)

  with st.spinner("Finding Skill Gaps..."):
    gaps = ask_ollama(f"Analyze this resume and highlight missing skills, certification, and experiences needed for better job opportunities: \n\n{resume_text}",max_tokens=400,)  

  with st.spinner("Future Roadmap..."):
    roadmap = ask_ollama(f"Based on this resume, suggest a future roadmap to improve this : \n\n{resume_text}",max_tokens=400,)


   #Display Result
  st.markdown("---")
  st.header("Resume Summary")
  st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size: 16px; color:white '>{summary}</div>", unsafe_allow_html=True)

  st.markdown("---")
  st.header("Skill Gaps and Missing Areas")
  st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size: 16px; color:white '>{gaps}</div>", unsafe_allow_html=True)

  st.markdown("---")
  st.header("Future Roadmap and Preparation Strategy")
  st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size: 16px; color:white '>{roadmap}</div>", unsafe_allow_html=True) 

  st.success("Analysis Complete Successfully!")


  if st.button("Get Job Recommendation"):
    with st.spinner("Fetch job recommendation..."):
      keywords = ask_ollama(
        f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma-seperated list only, no explanation. \n\n: {summary}, max_token=100"
      )

      search_keywords_clean = keywords.replace("\n", "").strip()

    st.success(f"Extracted job keywords: {search_keywords_clean}")

    with st.spinner("Fetch Jobs from LinkedIn and Naukri..."):
      linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=5)
      naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=5)


    st.markdown("---")
    st.header("Top LinkedIn Jobs")

    if linkedin_jobs:
      for job in linkedin_jobs:
        st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}")
        st.markdown(f"- 📍{job.get('location')}")
        st.markdown(f"- 🔗[View Job]({job.get('link')})")
        st.markdown("---")
    else:
      st.warning("No Linkedin Jobs found")



    st.markdown("---")
    st.header("Top Naukri Jobs")
    
    if naukri_jobs:
      for job in naukri_jobs:
        st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}")
        st.markdown(f"- 📍{job.get('location')}")
        st.markdown(f"- 🔗[View Job]({job.get('link')})")
        st.markdown("---")
    else:
      st.warning("No Naukri Jobs found")