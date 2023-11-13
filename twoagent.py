from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "codingaemo"})
# user_proxy.initiate_chat(assistant, message="create a csv file for daily temperatures in sydney for the month of sept and oct 2023")

user_proxy.initiate_chat(assistant, message="Plot a chart of the electricity price and weather for just NSW along with a forecast for the rest of the month. The current directory has two csv files called AEMOAvgpriceSep20.csv and AEMOAvgpriceOct20.csv which has this info. There is also a csv file called TempSeptOct.csv that has the weather data for that period. merge these datasets and use the merged data to forecast the last week of october. fbprophet is now called prophet so use from prophet import Prophet in the code instead of fbprophet.")


#user_proxy.initiate_chat(assistant, message="Plot a chart of microsoft and aws stock price change YTD for the last 3 years.")


#user_proxy.initiate_chat(assistant, message="Plot a chart of two organizations stock price change YTD for the last 3 year in a webpage based on user input")

#user_proxy.initiate_chat(assistant, message="Plot a chart of McDonalnds and Starbucks capitilization over the past two years.")
#user_proxy.initiate_chat(assistant, message="Plot a chart of MSFT and Google stock price change YTD for the last 3 years.")
#user_proxy.initiate_chat(assistant, message="Plot a chart of cancer cases by LHD boundaries for NSW Australia.")

#user_proxy.initiate_chat(assistant, message="Does the number of doctors per capita influence the number of COVID-19 cases? If so, how?")