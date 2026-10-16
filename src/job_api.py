
from apify_client import ApifyClient
import os
from dotenv import load_dotenv
load_dotenv()


apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))



#fetch linkedin job based on search query and location
def fetch_linkedin_jobs(search_query, location="india", rows=5):
  run_input={
    "keyword":search_query,
    "location":location,
    "rows":rows,
    "proxy":{
      "useApifyProxy": True,
      "apifyProxyGroups":["RESIDENTIAL"],

    }
  }
  run = apify_client.actor("hKByXkMQaC5Qt9UMN").call(run_input=run_input)
  jobs =list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
  return jobs[:rows]

#fetch Naukri job based on search quary and location
def fetch_naukri_jobs(search_query, location="india", rows=5):
  run_input={
      "keyword":search_query,
      "maxJobs":rows,
      "freshness":"all",
      "sortBy":"relevance",
      "experience":"all",
  
  }
  run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
  jobs =list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
  return jobs[:rows]