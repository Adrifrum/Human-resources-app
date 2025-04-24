from dash import dcc, register_page
from components import Box

register_page(
    __name__,
    path='/aboutus',
    title='A propos'
)


layout = [
    Box(
        title="A propos",
        children=[
            dcc.Markdown("""
            ## 🔍 About the Project

            This dashboard was developped by Adrien FRUMENCE with open-source technologies (Python/Dash/Digital ocean public cloud). It provides real-time insights into key human resources indicators for the OECD, focusing on employee turnover, attrition, and sentiment analysis. Designed to support data-driven HR decision-making, the platform enables a clear and dynamic view of workforce trends within the organization.

            ### 💡 Key Features:
            - **Turnover and Attrition Rates**: Automatically calculated and visualized using up-to-date internal data, enabling tracking of workforce changes by department and over time.
            - **Sentiment Analysis**: Leveraging employee reviews from platforms like Glassdoor, the system uses natural language processing to provide a live pulse on employee morale and engagement.
            - **Interactive Visualizations**: Built with Python and Dash, the dashboard presents data in an intuitive and interactive format, including gauges, line charts, and heatmaps.
            - **Open Source Technology**: The entire platform is developed using open-source tools, ensuring flexibility, transparency, and cost-efficiency.
            - **Cloud Deployment**: Hosted on a public cloud infrastructure for secure, scalable, and always-on access.

            This project reflects a commitment to transparency, innovation, and proactive HR strategy. It offers a modern approach to workforce analytics tailored to the unique needs of an international organization like the OECD.

            ---

            📬 I would be honored to receive your feedback on this tool.  
            Feel free to reach out to me at  
            [adrien.frum@gmail.com](mailto:adrien.frum@gmail.com?subject=Feedback%20on%20portfolio%20tool%20%3A%20OECD%20application).
            """)
        ]
    )
]