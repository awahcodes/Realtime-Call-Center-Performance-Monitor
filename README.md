# Commits and files in master

OVERVIEW:

In a highly competitive market, businesses must continuously optimize internal processes to maintain relevance. This analysis evaluates key performance metrics of a call center, focusing on Average Call Time, Average Handling Time, Average Call Rating, and Closed Call Status.

APPROACH:

•	Data for over 10 countries' call centers, including call times, response times, call status, and ratings, was generated using Python.
•	A structured database was created in MySQL and captured information on locations, companies, issues, call statuses, and customer service representatives.
•	Data flow from Python to MySQL was established via MySQL connectors, with a DirectQuery connection between MySQL and Power BI to ensure real-time data updates.
•	Power BI was used for analysis, modeling, and creating dashboards to visualize performance.

INSIGHTS:

•	Average response time exceeded the target of 120 seconds.
•	Average call duration met the target of 300 seconds.
•	Average call rating was below the target of 9, with a score of less than 5.
•	Approximately 75% of inbound calls were not resolved on the first attempt, being either referred, transferred, or declined.
•	Most locations averaged a rating score of ≤ 6.0.

RECOMMENDATIONS:

•	Response Time: Longer response times may indicate inefficiencies in the IVR system or a shortage of available representatives. Reducing IVR length or increasing staffing may improve response times.
•	Call Rating & Resolutions: The low rating reflects the high volume of unresolved calls. Empowering representatives to make decisions, reducing transfers (30% of calls were transferred), and improving IVR clarity could enhance first-call resolution and improve ratings.
•	Team Lead Dependency: With 25% of calls requiring team lead decisions, better equipping representatives could help resolve issues faster and improve customer satisfaction.

