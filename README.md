# Lead Scraping & Outreach Automation System

## Overview
This project automates the process of scraping relevant job titles from LinkedIn based on companies and geographies submitted through a form, filtering the data based on experience and job seniority, retrieving contact details via Apollo.io, and pushing qualified leads to a Google Sheet and integrated outreach tools such as Instantly and AI calling/SMS systems.

## Objectives
1. Users submit a list of companies and country targets via a form.
2. System scrapes all relevant job titles from LinkedIn associated with those companies.
3. Users select the relevant titles via a second form.
4. The system retrieves individuals matching the selected job titles.
5. Contact information (emails, and optionally phone numbers) is fetched via [Apollo.io](https://www.apollo.io/).
6. Results are stored in a shared Google Sheet.
7. Leads are added to:
   - **Instantly** for automated emailing.
   - **AI caller tools** for SMS and voice call outreach.

## Key Features
- Filters for:
  - Country-specific employees.
  - People with **6-10+ years of total work experience** (not limited to current company).
  - Seniority levels: **CEO, CXO, Vice President, Principal, Director, Manager, Owner**.
  - **Former employees** must have left within the **last 5 years**.
- Integration with GPT to screen job titles for relevance.
- VLOOKUP on client domain:
  - If domain is found: scrape both **emails and phone numbers**.
  - If not found: scrape **emails only**.
- Two contact extraction options:
  - Option 1: Emails + phone numbers (if domain found).
  - Option 2: Emails only (fallback).
- High-speed scraping using:
  - **BeautifulSoup**, **Selenium**, **BrightData**, **Soax**, **Apify**, **ProxyCurl**, **Oxylabs**.
- Ability to process many requests simultaneously.
- AI-based engagement follow-up:
  - If no reply to email/SMS within 12 hours, initiate AI voice call.

## Workflow Description
### Form 1: Company Input
- [Form 1 - Company List & Geography](https://forms.zohopublic.eu/consultancyinternational/form/NewProjectClientformtoCheckRelevantTitlesfromTarge/formperma/P0GGeTZoZFPy4r2B725Vy0jrR7evkSszpnxz4YASrbw)
1. Company and geo data submitted via Form 1.
2. Stored in Google Sheets tab: **Form 1 Titles Request**.
3. Script fetches relevant job titles from LinkedIn.
4. Titles appear in column M of the sheet.

### Form 2: Title Selection
- [Form 2 - Title Selection](https://forms.zohopublic.eu/consultancyinternational/form/Clientformtochooserelevanttitlespercompany/formperma/XNw0yYl0dFipamc2XZkKZtPDuoTO_HOsvJ_H9I3aWVE)
1. User selects preferred job titles for each company.
2. Stored in Google Sheets tab: **Form 2 - Chosen Relevant Titles**.
3. Script fetches matching individuals from LinkedIn.
4. Results populated in **Form 2 - Results** tab.
5. Contact details (emails) appear in **Form 2 - Emails Found** tab.

## Data Output
- [Google Sheet - Output Dashboard](https://docs.google.com/spreadsheets/d/1j4T361WjsHzZFG86cwXUVP1Qhi7i-XuQCBhCagmp4h8/edit?gid=0#gid=0)

## Technologies Used
- **Frontend Forms**: Zoho Forms
- **Data Storage & Logic**: Google Sheets + Apps Script
- **Scraping**: LinkedIn via BeautifulSoup, Selenium, Apify, Oxylabs, BrightData, ProxyCurl
- **Contact Extraction**: Apollo.io API
- **Enrichment & Outreach**:
  - Google Sheets VLOOKUP logic
  - Instantly emailing
  - AI Caller & SMS tool (2 systems integrated)
- **AI Integration**: ChatGPT API to validate relevance of job titles

## Challenges Addressed
- Handling both **current and former employees**, with filtering logic for recency and experience.
- Speed: Existing system in Make.com is slow — this solution aims for execution in **seconds**.
- Scalability: Capable of handling **high volume** of form submissions simultaneously.
- Customizable outreach sequences using conditions and AI-driven follow-up.

## Future Improvements
- Add a user dashboard to track progress and submitted leads.
- Real-time feedback in forms after submission.
- Webhook-based Zapier/Make replacement for full control and speed.
- Export to CSV/PDF options for reporting.

---
For any questions or implementation help, feel free to open an issue or contact the repository maintainer.

