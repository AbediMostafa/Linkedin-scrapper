from pprint import pprint
import time
from scraper.client import Client, people_query_factory

kwargs = {'cookie': 'bcookie="v=2&272fc227-a2b9-49e2-8875-1ada124cef4c"; bscookie="v=1&202504081217029108937d-e552-46a8-8adb-fc23cc5a476cAQH6hQtlOI-To0JLi_Gv-MBmkJ_BZcW9"; lang=v=2&lang=en-us; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; g_state={"i_l":0}; liap=true; li_at=AQEDAVlzkc8ArxcuAAABlhVV3i8AAAGWOWJiL04AN8uGyWMvAPmemXjWiw4LLpwEz71iSV-ErGpeaEDC_e6NuVu2R3joMVIgUo0mVbm7XIoIcNAvgcyJq9Jn5bNqMbBgbIAcx-TesHw1k7p-AwPlbnqS; JSESSIONID="ajax:8291769166855438411"; timezone=Asia/Tehran; li_theme=light; li_theme_set=app; li_sugr=19d51fef-112d-4269-9b67-1255e763f573; _guid=944d2977-8a66-4c63-8842-3eacf9d8970b; AnalyticsSyncHistory=AQKnazWR4xgingAAAZYVViGPuGGUx8chYXi3rXkomMv4vupzaz8Jeiak3jYXkdczfuXkZ-tVvhmpbQBHIhH2Pw; dfpfpt=b6a40cb5fd3f435a9c24398fde1f7782; _gcl_au=1.1.783251026.1744114689; lms_ads=AQE3usPF-6Re4AAAAZYVViNqLMxLKj9Pj6L0IzYuYDNTm5EAt7e734Ybf_P8fsWnabLZKRvEmCg9DOVnD2JeXRLQhfRbpxZV; lms_analytics=AQE3usPF-6Re4AAAAZYVViNqLMxLKj9Pj6L0IzYuYDNTm5EAt7e734Ybf_P8fsWnabLZKRvEmCg9DOVnD2JeXRLQhfRbpxZV; fptctx2=taBcrIH61PuCVH7eNCyH0MJojnuUODHcZ6x9WoxhgCl7EmIiFHFE3yxGZ1SjCewrzz31nVAEAx3rEUoCIG7MprnQNJJ7qxsMITGO9vAySPBPPcsJs6fxrWJozb1HQBoNtPV9Eg8hnBHH1UwDht5kt68j4U7H%252b452ijm3u65EPU1OtSQ1YdAm2QvdBdR3DLPJdbPwU5zm2L9IZgWrBXBlPepG%252bbPgnWmj%252fxSZkAnnyKa7y7mJXW%252b5AaR0IPXriwqiXzEny1kM66Q0FS40HRNE170iqA4xYN6KfGTow2PiXvuPknlGyDMUImIkud0xCGFVAYDM9GKUtdix%252b8EAB4xbWIsLYf4lzOkKa4%252bKEgaQUWQ%253d; __cf_bm=4FIHO.WxeErmjNZEBvFfdn9plMCheyfyQIdj2tIkVWM-1744115112-1.0.1.1-8wQCRc3PM50dRrVdW0dzif_WpZ7yz5NbjP82OZEjWhzfYltylcepMbE9FeKUWsxbZKmMhtE3N6yqSREJhXrBLgNevA7DnPvpWVBm6cCKeX4; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20187%7CMCMID%7C90267480142822205953981483246683095351%7CMCOPTOUT-1744122822s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C400281722%7CMCAAMLH-1744720422%7C6%7CMCAAMB-1744720422%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; aam_uuid=90461442442371952564003206215026209532; li_mc=MTsyMTsxNzQ0MTE1NzE0OzI7MDIxEldFLzRbC1+T/L18jcDjvUW1W9jSgfZbhFg/CM+h9XM=; UserMatchHistory=AQK5kDi34c_pnQAAAZYVZcpmH5aEU8VktIYygjKV7Z02M8dFP1-_mtjkADQ48lLsbh1Kab4YfeR_ChdV0keA_d9BnC5Wt5EusH884GJ_NEA_A5SnhB0hXzw5CatJ1r6YD76CmrpaEYt7F3f57XsRxoARSLWlKtb732Ya7Y-Gbpt_EVCIwh3Vy76xd2eEbWpNb-oni7NTSHbV2fPHdxlnUzYtvFDx9wBxe_T3kIocILx_VaHY_jAQ11Qap6zLon3Kh3vjv32E12aifHHNTpZoIjEMH8hASxRDLLDKOwghnzbXf7Q0XQUNpniFGB3UpJ-LcsEXfwpRqtWgTcKmDLfIY4RvIVFUAybQVjwcTeFqgGYAHkWj1A; lidc="b=TB91:s=T:r=T:a=T:p=T:g=5996:u=1:x=1:i=1744115716:t=1744144130:v=2:sig=AQEaXwjItnBUyz7gh-KgQXNaCifjP2DK"',
'csrf_token': 'ajax:8291769166855438411',}
queries = people_query_factory(50, company_name='meta')

client = Client()
# pprint(client._session.headers)
pprint([str(q) for q in queries[:]])
for q in queries:
    response = client.execute(str(q))
    time.sleep(1)
    print(response.status_code, response.json())
